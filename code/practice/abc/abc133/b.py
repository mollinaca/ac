#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n,d = map(int,input().split())
c=0
pos={}
for i in range(n):
    pos[i]=list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        x = 0
        for k in range(d):
            x += (abs(pos[i][k]-pos[j][k]))**2
        if (math.sqrt(x)).is_integer():
            c += 1

print (c)
