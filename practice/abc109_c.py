#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fractions
from functools import reduce
n,x = map(int,input().split())
x_list = list(map(int,input().split()))
if n == 1:
    print (abs(x_list[0]-x))
    exit (0)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

y_list = []
for i in x_list:
    y_list.append(abs(i-x))

print (gcd_list(y_list))