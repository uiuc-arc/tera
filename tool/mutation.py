#!/usr/bin/env python3
# python3 mutation.py [repo name] [#tests-optional]
import sys
import testspecs
import libraries
import re

repo=sys.argv[1]

# create test command
all_specs = [s for s in testspecs.testspecs if s.repo == repo]
if len(sys.argv) > 2:
    all_specs = all_specs[:int(sys.argv[2])]

def get_relative_filename(filename):
    return re.sub("/projects/[^/]+/", "", filename.replace(libraries.PROJECT_DIR, ""))

def pytest_string(specs, suffix=""):
    r = ""
    for s in specs:
        if s.skip:
            continue

        if "none" in s.classname:
            r = r + "{0}::{1}{2}".format(get_relative_filename(s.filename), s.testname, suffix) + " "
        else:
            r = r + "{0}::{1}::{2}{3}".format(get_relative_filename(s.filename), s.classname,  s.testname, suffix) + " "
    return r
print(pytest_string(all_specs))