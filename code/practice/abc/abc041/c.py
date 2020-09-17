#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
d = {}
for i in range(1,n+1):
    d[i] = a[i-1]

d = sorted(d.items(), key=lambda x:x[1], reverse=True)
for i in d:
    print (i[0])
