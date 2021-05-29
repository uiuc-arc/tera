import multiprocessing
import shutil
import subprocess as sp

from src.lib import TestSpec


class BaseRunner:
    def __init__(self, spec:TestSpec, condaenvname, libdir):
        self.spec=spec
        self.condaenvname = condaenvname
        self.libdir=libdir
        self.exec_timeout=None

    def set_parameter(self, param, value):
        with open(self.spec.filename) as f:
            c = f.read()
            # matching both quotes
            c = c.replace("'<{0}>'".format(param), str(value))
            c = c.replace("\"<{0}>\"".format(param), str(value))
        with open(self.spec.filename, "w") as f:
            f.write(c)

    def run_pytest(self, i) -> (str, str):
        try:
            # start=time.time()
            # info=resource.getrusage(resource.RUSAGE_CHILDREN)
            result = sp.run(['time -f "\t%U user,\t%S sys" {4}/tool/src/runtest.sh {0} {1} {2} {3} {5}'.format(
                self.spec.filename,
                self.spec.classname,
                self.spec.testname,
                self.condaenvname,
                self.libdir,
                i % multiprocessing.cpu_count()
            )],
                            shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
            sys_exec_time = float(str(result.stderr).strip().rpartition('t')[2].rpartition('sys')[0].strip())
            user_exec_time = float(str(result.stderr).strip().rpartition('user')[0].rpartition('t')[2].strip())
            #print(info)
            #print(info2)
            #total_time=(info2.ru_utime+info2.ru_stime) - (info.ru_utime+info.ru_stime)
            #total_time=time.time()-start
            #sys_exec_time = float(sys_exec_time)
            total_time = sys_exec_time + user_exec_time
        except:
            import traceback as tb
            tb.print_exc()
            return "".encode(), "TimeoutExpired".encode(), 1, 10000
        return result.stdout, result.stderr, result.returncode, total_time

    def run_test(self, i):
        output, error, returncode, total_time = self.run_pytest(i)
        return output, error, returncode, total_time

    def save_temp(self):
        shutil.copy(self.spec.filename, self.spec.filename + ".tmp")

    def restore(self):
        shutil.move(self.spec.filename + ".tmp", self.spec.filename)
