#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:10:02 2018

@author: shimac
"""

# Quick Python Overview
#   Chapter 3

#-------------------------------------------------------
# pp.19 ----------------------------------------- numbers
# divide
5/2
# divide, for truncated integer results
5//2
# modulus
5 % 2
# exponents
2 ** 4
# multiplication with complex numbers
x = (3+2j) * (4+9j)
x
x.real
x.imag
# rounding
round(3.49)
# ceiling
import math
math.ceil(3.49)
# bool
x = False
x
not(x)
not x

#-------------------------------------------------------
# pp.21 ----------------------------------------- Lists
# lists can contain mixed types of elements
x = ["first", "second", "third", "fourth", 5, 6, 7, 8]
x[0]
x[7]
x[:-2]
x[-2:]
x[-2:-1]
# lists are mutable, you can change shit later
x[1] = "balls!!!"
x
# list functions: min, max, len, reverse, count, append, extend, index, insert, pop, remove, sort
len(x)
x.reverse()
x
x + x
x

#-------------------------------------------------------
# pp.22 ----------------------------------------- Tuples
# immutable
x = [1, 2, 3, 4]
tuple(x)
y = (4, 5, 6, 7)
list(y)

#-------------------------------------------------------
# pp.23 ----------------------------------------- Strings
