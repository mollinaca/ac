#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k,m = map(int,input().split())
A = list(map(int,input().split()))
x = (m*n)-sum(A) 
if x < 0:
    print (0)
elif x <= k:
    print (x)
else:
    print (-1)
