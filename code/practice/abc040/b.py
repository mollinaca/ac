#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
m = n**2

if n == 1:
    print (0)
    exit ()

for i in range(1,n):
    x = n//i
    y = n - x*i
    if abs(i-x) + y < m:
        m = abs(i-x) + y
print (m)
