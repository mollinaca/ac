#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
p = list(map(int,input().split()))

c = 0
next_skip=False
for i in range(1,len(p)+1):

    if next_skip:
        next_skip=False
        continue

    if p[i-1] == i:
        c+=1
        next_skip=True

print (c)
