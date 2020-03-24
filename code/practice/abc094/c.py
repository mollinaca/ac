#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
x = list(map(int,input().split()))
y = sorted(x)
lidx = n//2
sidx = lidx-1
for v in x:
    if v <= y[sidx]:
        print (y[lidx])
    else:
        print (y[sidx])
