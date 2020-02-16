#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
d = {}
for _ in range(n):
    s = input()
    if not s in d:
        d[s] = 1
    else:
        d[s] += 1
d_max = max(d.values())
ans = [k for k, v in d.items() if v == d_max]
for a in sorted(ans):
    print (a)
