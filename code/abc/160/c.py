#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k,n = map(int,input().split())
a = list(map(int,input().split()))
a.append(k+a[0])
d=0
for i in range(len(a)-1):
    if i == len(a):
        break
    else:
        if d < a[i+1] - a[i]:
            d = a[i+1] - a[i]
print (k-d)