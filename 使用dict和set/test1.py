#!/usr/bin/env python3

#-- coding utf-8 --

d = {'a':1, 'b':2, 'c':3}

print(d)

print('a' in d)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1 & s2)

print(s1 | s2)

s3 = (1, 2, 3)

d2 = {s3:1}

print((1, 2, 3) in d2)

print(d2.(1, 2, 3))