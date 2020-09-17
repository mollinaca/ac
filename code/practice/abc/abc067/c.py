#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int,input().split()))
total = sum(a)
ans = float('inf')
x = 0
for i in range(N-1):
    x += a[i]
    ans = min(abs(total-2*x),ans)
print (ans)
