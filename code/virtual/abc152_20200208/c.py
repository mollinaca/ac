#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
p = list(map(int,input().split()))

min_p = p[0]
count = 0
for i in range(len(p)):
    if p[i] <= min_p:
        count += 1
        min_p = p[i]

print (count)