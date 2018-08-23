#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for udmover.
"""

import setuptools
import os
import udmover


def setup_package():
    homedir = os.environ['HOME']
    setuptools.setup(
        version=udmover.__version__,
        packages=setuptools.find_packages(),
        entry_points={
           'console_scripts': [
               'udmover = udmover.udmover:main'
           ]
        },
        data_files={
            'etc/udmover/udmover.conf.sample = ~/udmover/udmover.conf.sample'
        }
    )


if __name__ == "__main__":
    setup_package()
