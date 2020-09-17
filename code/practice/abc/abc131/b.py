#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,l = map(int,input().split())
azi = (l-1)*n + (n*(n+1))//2
x = []
y = []
for i in range(1,n+1):
    x.append(l+i-1)
    y.append(abs(l+i-1))
print (azi-x[y.index(min(y))])
