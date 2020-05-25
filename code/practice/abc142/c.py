#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
d = {}
for i,a in zip(range(1,n+1),A):
    d[a] = i
d = sorted(d.items())

for t in d:
    print (t[1], end=" ")
