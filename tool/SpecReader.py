import hashlib

from src.lib.AssertType import AssertType


class SpecReader:
    def __init__(self):
        self.repo = None
        self.filename = None
        self.classname = None
        self.testname = None
        self.param_line = None
        self.param_col = None
        self.param_type = None
        self.param_default = None
        self.assertLine = None
        self.assertType = None

    @staticmethod
    def read(entry):
        specReader = SpecReader()
        e=entry.split(",")
        specReader.repo=e[0]
        specReader.filename=e[1]
        specReader.classname=e[2]
        specReader.testname=e[3]
        specReader.param_line=int(e[4])
        specReader.param_col=int(e[5])
        specReader.param_type=e[6]
        specReader.param_default=e[7]
        specReader.assertLine=int(e[8])
        specReader.assertType=AssertType.get_assert_type(e[9])
        return specReader

    def get_hash(self):
        s = '_'.join([self.filename, self.classname, self.testname, str(self.param_line), str(self.param_col), str(self.assertLine),
                      ]).encode("utf-8")
        return str(int(hashlib.sha1(s).hexdigest(), 16) % (10 ** 8))


