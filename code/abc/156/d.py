#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n,a,b = map(int, input().split())

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

total = 0
for i in range(n):
    if i == a or i == b:
        continue
    total += combinations_count(n,i)

print (total%(10**9+7))