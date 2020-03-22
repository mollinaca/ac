#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    total = 0
    x = a.copy()
    del x[i]
    x = collections.Counter(x)
    for v in x.values():
        total += v*(v-1)//2
    print (total)
