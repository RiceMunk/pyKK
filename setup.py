#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# This is a customised setup.py based on the astropy-helpers setup.py

from distutils.core import setup

import sys

from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [
      ('pytest-args=', 'a', "Arguments to pass to py.test"),
      ('coverage', 'c', "Does coverage testing"),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# Get some values from the setup.cfg
from distutils import config
conf = config.ConfigParser()
conf.read(['setup.cfg'])
metadata = dict(conf.items('metadata'))

PACKAGENAME = metadata.get('package_name', 'packagename')
DESCRIPTION = metadata.get('description', '')
AUTHOR = metadata.get('author', '')
AUTHOR_EMAIL = metadata.get('author_email', '')
LICENSE = metadata.get('license', 'unknown')
URL = metadata.get('url', '')

# VERSION should be PEP386 compatible (http://www.python.org/dev/peps/pep-0386)
VERSION = '0.1dev'

# Indicates if this version is a release version
RELEASE = 'dev' not in VERSION

setup(name=PACKAGENAME,
      version=VERSION,
      py_modules=[PACKAGENAME],
      cmdclass = {'test': PyTest},
      )
