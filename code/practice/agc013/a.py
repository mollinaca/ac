#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int, input().split()))

inc = None
c = 0
 
for i in range(n-1):
    if inc == None:
        if A[i] == A[i+1]:
            pass
        elif A[i] < A[i+1]:
            inc = True
        else:
            inc = False
    elif inc:
        if A[i] > A[i+1]:
            c += 1
            inc = None
    else:
        if A[i] < A[i+1]:
            c += 1
            inc = None

print(c+1)
