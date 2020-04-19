#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = sorted(list(map(int,input().split())))
d = {}
for i in range(1,n+1):
    d[i] = 0

for v in A:
    d[v] += 1

for v in d.values():
    print (v)
