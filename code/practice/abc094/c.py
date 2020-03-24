#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
x = list(map(int,input().split()))
y = sorted(x)
lx = len(x)
lxi = (lx-1)//2
for v in x:
    z = y.copy()
    z.remove(v)
    print (z[lxi])
