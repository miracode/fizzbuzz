#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The module provides two function, fizzbuz and fizzbuz_extended
"""

def fizzbuzz(n):
    """return a fizzbuzz-formatted representation of n"""
    if n == 0:
        return str(0)
    out = ''
    data = [(3, 'Fizz'), (5, 'Buzz')]
    for divisor, replacement in data:
        if not n % divisor:
            out += replacement
    if not out:
        out = str(n)
    return out
