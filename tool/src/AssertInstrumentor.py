import ast
from ast import *

import astunparse

from src.lib.AssertSpec import AssertSpec
# ast nodes
from src.lib.AssertType import AssertType

numpy_import = ast.Import(names=[ast.alias(name='numpy', asname='np')])
torch_import = ast.Import(names=[ast.alias(name='torch', asname=None)])
pytest_import = ast.Import(names=[ast.alias(name='pytest', asname=None)])
tensorflow_import = ast.Import(
    names=[ast.alias(name='tensorflow', asname='tf')])
sys_import = ast.Import(names=[ast.alias(name='sys', asname=None)])

string_formatter = '''
def sample_to_string(mystr):
    if isinstance(mystr, list):
        return "[{0}]".format(','.join([sample_to_string(i) for i in mystr]))
    if isinstance(mystr, np.ndarray):
        return np.array2string(mystr, max_line_width=np.inf, precision=100, separator=',', threshold=np.inf).replace('\\n', '')
    try:
        mystr = np.array(mystr)
        return np.array2string(mystr, max_line_width=np.inf, precision=100, separator=',', threshold=np.inf).replace('\\n', '')
    except:
        pass
    try:
        if isinstance(mystr, torch.Tensor):
            return np.array2string(mystr.detach().numpy(), max_line_width=np.inf, precision=100, separator=',',
                                   threshold=np.inf).replace('\\n', '')
    except:
        pass
    try:
        if isinstance(mystr, tf.Tensor):
            with tf.Session():
                return np.array2string(mystr.eval(), max_line_width=np.inf, precision=100, separator=',', threshold=np.inf).replace(
                    '\\n', '')
    except:
        pass
    return str(mystr)
    '''


class AssertInstrumentor(ast.NodeTransformer):

    def __init__(self, spec: AssertSpec, logstring: str, deps: list, transformer=None):
        self.assert_spec = spec
        self.log_string = logstring
        self.dependencies = deps
        self.val = 1
        self.modified_ast = None
        self.transformer = transformer

    def _generate_seed_stub(self, varname, lib_alias, lib_func, seed_size):
        return [
            Assign(targets=[Name(id=varname, ctx=Store())], value=Call(
                func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()),
                               attr='randint',
                               ctx=Load()), args=[Attribute(
                                   value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='iinfo', ctx=Load()),
                                              args=[Attribute(value=Name(
                                                  id='np', ctx=Load()), attr=seed_size, ctx=Load())],
                                              keywords=[]),
                                   attr='max', ctx=Load())], keywords=[])),
            Expr(value=Call(
                func=Attribute(value=Name(id=lib_alias, ctx=Load()),
                               attr=lib_func, ctx=Load()),
                args=[Name(id=varname, ctx=Load())], keywords=[])),
            Expr(
                value=Call(func=Name(id='print', ctx=Load()),
                           args=[BinOp(left=Str(s='\n{0} seed: %s'.format(lib_alias)),
                                       op=Mod(),
                                       right=Name(id=varname, ctx=Load()))],
                           keywords=[]))

        ]

    def _create_string_formatter(self):
        string_formatter_nodes = ast.parse(string_formatter)
        return string_formatter_nodes.body[0]

    def _create_fixture(self):
        body = []
        if 'numpy' in self.dependencies:
            body = body + \
                self._generate_seed_stub(
                    'npseed', 'np.random', 'seed', 'int32')
        if 'torch' in self.dependencies:
            body = body + \
                self._generate_seed_stub(
                    'torchseed', 'torch', 'manual_seed', 'int64')
        if 'tensorflow' in self.dependencies:
            trypart = self._generate_seed_stub(
                'tfseed', 'tf', 'set_random_seed', 'int64')
            exceptpart = self._generate_seed_stub(
                'tfseed', 'tf.random', 'set_seed', 'int64')
            body = body + [Try(body=trypart, orelse=[], finalbody=[], handlers=[
                ast.ExceptHandler(type=Name(id='Exception', ctx=Load()), name=None, body=exceptpart)])]
        fixture_func = ast.FunctionDef(
            name='show_guts',
            args=ast.arguments(
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[]),
            body=body,
            decorator_list=[
                Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[],
                     keywords=[keyword(arg='scope', value=Str(s='session'))])],
            returns=None)

        return fixture_func

    def instrument(self):

        # instrument child class or the main class (if no base class)
        with open(self.assert_spec.test.filename) as file:
            fileast = ast.parse(file.read())

            modified = self.visit(fileast)
            modified = ast.fix_missing_locations(modified)

            # find position of class def.. insert before first class def
            # of first function def (allowing for files with import __future__
            pos = [i for i in range(len(modified.body)) if isinstance(
                modified.body[i], (ast.ClassDef, ast.FunctionDef))]
            if len(pos) == 0:
                pos = [0]
            pos = pos[0]
            # allow only if either no base class or base class in same file

            str_formatter = self._create_string_formatter()
            modified.body.insert(pos, str_formatter)

            modified.body.insert(pos, pytest_import)
            modified.body.insert(pos, sys_import)
            if 'numpy' in self.dependencies:
                modified.body.insert(pos, numpy_import)
            if 'torch' in self.dependencies:
                modified.body.insert(pos, torch_import)
            if 'tensorflow' in self.dependencies:
                modified.body.insert(pos, tensorflow_import)

            self.modified_ast = modified

    def write_file(self):
        # write new file
        with open(self.assert_spec.test.filename, 'w') as file:
            file.write(astunparse.unparse(self.modified_ast).strip())

    def get_print_stmt(self, node):
        repl_node = Assign(targets=[Name(id='val_{0}'.format(self.val), ctx=Store())],
                           value=node)
        if "pytorch-deps\garage" in self.assert_spec.test.filename:
            print_node = ast.parse(
                "sys.stderr.write(('{0}%s\n' % sample_to_string({1}) ))".format(self.log_string,
                                                                                'val_{0}'.format(self.val)))
        else:
            print_node = ast.parse(
                "print(('{0}%s' % sample_to_string({1}) ))".format(self.log_string,
                                                                   'val_{0}'.format(self.val)))
        self.val += 1
        return [repl_node, print_node]

    def visit(self, node):
        if isinstance(node, ast.Expr):
            if isinstance(node.value, ast.Call):
                if isinstance(node.value.func, ast.Name):
                    if node.lineno != self.assert_spec.line and self.assert_spec.line != -1:
                        return node
                    stmt = []
                    if AssertType.get_assert_type(node.value.func.id) is not None:
                        # asserts with compare exp inside
                        if node.value.func.id in ['assertTrue', 'assertFalse'] and isinstance(node.value.args[0],
                                                                                              ast.Compare):
                            printstmt = self.get_print_stmt(
                                node.value.args[0].left)
                            node.value.args[0].left = printstmt[0].targets[0]
                            stmt.extend(printstmt)
                            for i, c in enumerate(node.value.args[0].comparators):
                                printstmt2 = self.get_print_stmt(c)
                                stmt.extend(printstmt2)
                                node.value.args[0].comparators[i] = printstmt2[0].targets[0]
                                if self.transformer is not None:
                                    node = self.transformer(node)
                        else:
                            # asserts without compare exp inside
                            for i, c in enumerate(node.value.args):
                                if i < 2:  # only first two arguments
                                    printstmt = self.get_print_stmt(c)
                                    stmt.extend(printstmt)
                                    node.value.args[i] = printstmt[0].targets[0]
                                    if self.transformer is not None:
                                        node = self.transformer(node)
                    stmt.append(node)
                    return stmt
                elif isinstance(node.value.func, ast.Attribute):
                    if node.lineno != self.assert_spec.line and self.assert_spec.line != -1:
                        return node
                    stmt = []
                    if AssertType.get_assert_type(node.value.func.attr) is not None:
                        if node.value.func.attr in ['assertTrue', 'assertFalse'] and isinstance(node.value.args[0],
                                                                                                ast.Compare):
                            printstmt = self.get_print_stmt(
                                node.value.args[0].left)
                            node.value.args[0].left = printstmt[0].targets[0]
                            if self.transformer is not None:
                                node = self.transformer(node)
                            stmt.extend(printstmt)
                            for i, c in enumerate(node.value.args[0].comparators):
                                printstmt2 = self.get_print_stmt(c)
                                stmt.extend(printstmt2)
                                node.value.args[0].comparators[i] = printstmt2[0].targets[0]
                                if self.transformer is not None:
                                    node = self.transformer(node)
                        else:
                            for i, c in enumerate(node.value.args):
                                if i < 2:  # only first two arguments
                                    printstmt = self.get_print_stmt(c)
                                    stmt.extend(printstmt)
                                    node.value.args[i] = printstmt[0].targets[0]
                                    if self.transformer is not None:
                                        node = self.transformer(node)
                    stmt.append(node)
                    return stmt
        elif isinstance(node, ast.Assert):
            if node.lineno != self.assert_spec.line and self.assert_spec.line != -1:
                return node
            if isinstance(node.test, ast.Compare):
                stmt = []
                printstmt = self.get_print_stmt(node.test.left)
                node.test.left = printstmt[0].targets[0]
                stmt.extend(printstmt)
                for i, c in enumerate(node.test.comparators):
                    printstmt = self.get_print_stmt(c)
                    stmt.extend(printstmt)
                    node.test.comparators[i] = printstmt[0].targets[0]

                if self.transformer is not None:
                    node = self.transformer(node)
                stmt.append(node)
                return stmt
            elif isinstance(node.test, ast.Call):
                # assert return value of a function
                stmt = []
                for i, c in enumerate(node.test.args):
                    if isinstance(c, ast.Name):
                        printstmt = self.get_print_stmt(c)
                        node.test.args[i] = printstmt[0].targets[0]
                        stmt.extend(printstmt)
                    elif isinstance(c, ast.Compare):
                        printstmt = self.get_print_stmt(c.left)
                        c.left = printstmt[0].targets[0]
                        stmt.extend(printstmt)
                        for ii, cc in enumerate(c.comparators):
                            printstmt = self.get_print_stmt(cc)
                            stmt.extend(printstmt)
                            c.comparators[ii] = printstmt[0].targets[0]
                if self.transformer is not None:
                    node = self.transformer(node)
                stmt.append(node)
                return stmt

        self.generic_visit(node)
        return node
