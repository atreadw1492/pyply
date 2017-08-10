# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:46:50 2017

@author: atrea
"""

from setuptools import setup

setup(name='pyply',
      version='0.1',
      description="""Based largely off functions found in R, pyply provides syntax in a functional programming style to make data manipulation easier.
                     This is meant especially for those transitioning from R to Python.""",
      url='https://github.com/atreadw1492/pyply',
      author='Andrew Treadway',
      author_email='opensourcecoder11@gmail.com',
      license='',
      packages=['pyply'],
      install_requires = ['pandas','collections','functools'],
      zip_safe=False)