#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from udmover.skeleton import fib

__author__ = "Mario David"
__copyright__ = "Mario David"
__license__ = "Licensed under the Apache License, Version 2.0"
__version__ = "0.0.1"
__date__ = "2018"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
