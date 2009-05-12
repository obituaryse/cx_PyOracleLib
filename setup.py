"""Distutils script for cx_PyOracleLib.

To install:
    python setup.py install

"""

from distutils.core import setup

modules = [
        "cx_ExportData",
        "cx_ImportData",
        "cx_OracleDebugger",
        "cx_OracleEx",
        "cx_OracleUtils",
        "cx_PatchCommands"
]

packages = [
        "cx_OracleObject",
        "cx_OracleParser",
        "cx_OracleParser.full",
        "cx_OracleParser.simple"
]


setup(
        name = "cx_PyOracleLib",
        version = "2.5",
        description = "Set of Python modules for handling Oracle databases",
        license = "See LICENSE.txt",
        long_description = "Set of Python modules for handling Oracle " + \
                "databases and used by a number of Computronix projects, " + \
                "in particular the cx_OracleTools project",
        author = "Anthony Tuininga",
        author_email = "anthony.tuininga@gmail.com",
        url = "http://starship.python.net/crew/atuining",
        py_modules = modules,
        packages = packages)

