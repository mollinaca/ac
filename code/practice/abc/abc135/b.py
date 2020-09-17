#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
p = list(map(int,input().split()))
p2 = sorted(p)
c = 0
for i,j in zip(p,p2):
    if i != j:
        c += 1
print ("YES") if c == 0 or c == 2 else print ("NO")
