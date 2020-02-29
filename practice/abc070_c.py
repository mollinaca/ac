#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fractions
from functools import reduce

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

def lcm(a:int,b:int):
    return a // fractions.gcd(a, b) * b

def lcm_list(numbers):
    return reduce(lcm, numbers)

print (lcm_list(l))