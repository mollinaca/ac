#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k,s = map(int,input().split())
count = 0
for i in range(k+1):
    for j in range(k+1):
        z = s - (i+j)
        if 0 <= z and z <=k:
            count += 1
print (count)