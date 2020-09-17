#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter

n = int(input())
A = []
c = 0
for _ in range(n):
    A.append(int(input()))

for v in Counter(A).values():
    if v > 1: c += v-1
print (c)
