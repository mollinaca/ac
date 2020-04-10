#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
l = []
for _ in range(m):
    a,b = map(int,input().split())
    l.append([a,b])

a = []
b = []
for x in l:
    if x[0] == 1:
        a.append(x[1])
    if x[1] == n:
        b.append(x[0])

if set(a) & set(b):
    print ("POSSIBLE")
else:
    print ("IMPOSSIBLE")
