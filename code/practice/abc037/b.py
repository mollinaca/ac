#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,q = map(int,input().split())
L = [0 for i in range(n)]

for _ in range(q):
    l,r,t = map(int,input().split())
    L = L[0:l-1] + [t for i in range(r-l+1)] + L[r::]

for i in L:
    print (i)
