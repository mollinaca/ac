#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
d = {}
for _ in range(n):
    s = input()
    if not s in d:
        d[s] = 1
    else:
        d[s] += d[s]+1
print (max(d, key=d.get))
