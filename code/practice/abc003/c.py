#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
R = sorted(list(map(int,input().split())),reverse=True)
R2 = sorted(R[0:k])
rate = 0
for i in range(k):
    if R2[i] > rate:
        rate = (rate+R2[i])/2
print (rate)
