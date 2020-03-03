#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
p = [int(e) for e in input().split()]
count=0
p_min=p[0]

for i in range(n):
    if p[i] <= p_min:
        count+=1
        p_min=p[i]

print (count)
