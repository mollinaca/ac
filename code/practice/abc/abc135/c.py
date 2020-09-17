#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans += min(A[i],B[i])
    B[i] = B[i] - A[i]
    if 0 < B[i]:
        ans += min(A[i+1],B[i])
        if A[i+1] <= B[i]:
            A[i+1] = 0
        else:
            A[i+1] = A[i+1] - B[i]
print (ans)
