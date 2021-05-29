import re

from src.lib import TestSpec


class ParamInstrumentor:
    def __init__(self, spec:TestSpec):
        self.spec=spec

    def instrument(self):
        buffer_dict=dict() # line wise buffer
        for param in self.spec.params:
            filecontents=open(self.spec.filename).readlines()
            line=filecontents[param.param_line-1]
            if param.param_line not in buffer_dict:
                buffer_dict[param.param_line] = 0
            buffer=buffer_dict[param.param_line]
            nextindex=param.param_col+buffer
            while nextindex < len(line) and len(re.findall("[0-9.e-]", line[nextindex])) > 0:
                nextindex += 1
            prefix=line[:param.param_col+buffer] + "\"<{0}>\"".format(param.name)
            line=prefix + line[nextindex:]
            buffer += len(prefix) - nextindex
            buffer_dict[param.param_line]=buffer
            filecontents[param.param_line-1]=line

            with open(self.spec.filename, "w") as f:
                f.writelines(filecontents)

