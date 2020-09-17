#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
B = list(map(int,input().split()))
A = []
for i in range(len(B)):
    if i == 0:
        A.append(B[0])
        continue
    A.append(min(B[i-1],B[i]))
A.append(B[-1])
print (sum(A))
