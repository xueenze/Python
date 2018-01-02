#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(ord('A'));

x = b'123';

print(x);

b'\xe4\123'.decode('utf-8', errors='ignore');

print(len('中文'.encode('utf-8')));

print('Hi %s, you fuck %d' % ('enxueenze', 123));

s1 = 72
s2 = 85

r = (85 - 72) / 72 * 100

print('提升了 {.1f}%' % r)

