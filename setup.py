#!/usr/bin/env python

from setuptools import setup

setup(
    name='bandicoot',
    author='Yves-Alexandre de Montjoye',
    author_email='yvesalexandre@demontjoye.com',
    version="0.4",
    url="https://github.com/yvesalexandre/bandicoot",
    license="MIT",
    packages=[
        'bandicoot',
        'bandicoot.helper',
        'bandicoot.tests',
        'bandicoot.special'
    ],
    description="A toolbox to analyze mobile phone metadata.",
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics'
    ])
