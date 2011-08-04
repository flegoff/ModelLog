#!/usr/bin/env python

from distutils.core import setup

setup(name='ModelLog',
      version='1.0.1',
      description='Log something when a Django model is edited',
      author='Benoit Guina',
      author_email='benoit.guina@9h37.fr',
      url='http://www.9h37.fr/',
      package_dir={'': 'src'},
      packages=['modellog'],
     )
