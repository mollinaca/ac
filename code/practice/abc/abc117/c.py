#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
X = sorted(list(map(int,input().split())))
d = []
for i in range(len(X)-1):
    d.append(X[i+1]-X[i])
d.sort(reverse=True)
print (sum(d[n-1:]))
