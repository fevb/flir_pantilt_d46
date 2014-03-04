#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['flir_pantilt_d46'],
    package_dir={'': 'src'},
    requires=['rospy'],
    scripts=['bin/ptu_action_server.py']
)

setup(**d)
