#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
from distutils.core import setup, Command

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(name='pyKK',
      version='0.0.1dev',
      py_modules=['pyKK'],
      cmdclass = {'test': PyTest},
      )
