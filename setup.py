#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for udmover.
"""

import setuptools
import os
import udmover


def setup_package():
    dst = 'etc/udmover/'
    src = 'etc/udmover/udmover.conf.sample'

    setuptools.setup(
        version=udmover.__version__,
        packages=setuptools.find_packages(),
        entry_points={
           'console_scripts': [
               'udmover = udmover.udmover:main'
           ]
        },
        data_files=[(dst, [src])]
    )


if __name__ == "__main__":
    setup_package()
