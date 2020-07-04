#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))

if sum(A)%n != 0:
    print (-1)
    exit ()

z = sum(A)//n
ans = 0
for i in range(n-1):
    if not (sum(A[:i+1]) == z*(i+1) and sum(A[i+1:]) == z*(n-i-1)):
        ans += 1
print(ans)
