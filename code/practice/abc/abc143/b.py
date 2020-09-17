#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
n = int(input())
d = list(map(int,input().split()))

ans = 0
p = itertools.combinations(d,2)
for v in p:
    ans += v[0]*v[1]
print (ans)
