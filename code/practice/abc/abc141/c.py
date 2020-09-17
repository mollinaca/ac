#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k,q = map(int,input().split())

d = {}
for _ in range(q):
    a = int(input())
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

for i in range(1,n+1):
    if not i in d:
        if q < k:
            print ("Yes")
        else:
            print ("No")
    else:
        if k <= q-d[i]:
            print ("No")
        else:
            print ("Yes")
