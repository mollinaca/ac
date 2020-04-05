#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
r = []
b = []
for _ in range(n):
    x,c = map(str,input().split())
    if c == 'B':
        b.append(int(x))
    else:
        r.append(int(x))

for x in sorted(r):
    print (x)
for x in sorted(b):
    print (x)
