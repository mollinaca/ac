#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
n = int(input())
l = list(map(int,input().split()))
ans = 0

p = itertools.combinations(l,3)
for v in p:
    print (v)
    if v[0] < v[1] + v[2] and v[1] < v[0] + v[2] and v[2] < v[0] + v[1]:
        ans += 1

print (ans)
