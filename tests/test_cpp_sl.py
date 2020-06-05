#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for C++ module so.sl.
"""

import os
import sys

import numpy as np
import so
# create an alias for the binary extension cpp module
cpp = so.sl


def test_cpp_prod():
    a=2.0;
    b=3.0
    c = cpp.prod(a,b)
    assert c == a*b


#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_cpp_prod

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
