#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mixing_py2_py3_ros'],
)

setup(**d)
