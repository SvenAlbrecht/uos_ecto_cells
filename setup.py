#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()

d['packages'] = ['uos_ecto_cells']
d['package_dir'] = { '' : 'python' }
d['install_requires'] = []

setup(**d)
