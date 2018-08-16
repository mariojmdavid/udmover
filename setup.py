#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for udmover.
"""

import setuptools
import udmover


def setup_package():
    setuptools.setup(
        version=udmover.__version__,
        packages=setuptools.find_packages(),
        entry_points = {
           'console_scripts': [
               'udmover = udmover.udmover:main'
           ]
        }
    )


if __name__ == "__main__":
    setup_package()
