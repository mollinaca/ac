#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,t = map(int,input().split())
A = []
total = 0
for _ in range(n):
    A.append(int(input()))

for i in range(n-1):
    if A[i+1]-A[i] > t:
        total += t
    else:
        total += A[i+1]-A[i]

print (total+t)
