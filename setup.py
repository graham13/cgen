#!/usr/bin/env python
# -*- coding: latin1 -*-

from setuptools import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

setup(
        name="cgen",
        version="2013.1.2",
        description="C/C++ source generation from an AST",
        long_description="""
            See `documentation <http://documen.tician.de/cgen/>`_
            and `git tree <http://github.com/inducer/cgen>`_.
            """,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Other Audience',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Topic :: Software Development :: Libraries',
            'Topic :: Utilities',
            ],

        author="Andreas Kloeckner",
        author_email="inform@tiker.net",
        license="MIT",
        url="http://documen.tician.de/cgen/",

        packages=["cgen"],
        install_requires=[
            "pytools>=8",
            ],

        # 2to3 invocation
        cmdclass={'build_py': build_py})
