#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
n = int(input())
L = list(map(int,input().split()))

ans = 0
ans_l = []
for v in itertools.combinations(L,3):
    if v[0] != v[1] and v[0] != v[2] and v[1] != v[2]:
        if v[0] < v[1]+v[2] and v[1] < v[0]+v[2] and v[2] < v[0]+v[1]:
            ans += 1

print (ans)
