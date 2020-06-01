#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m,c = map(int,input().split())
b = list(map(int,input().split()))
ans = 0
for _ in range(n):
    a = list(map(int,input().split()))
    x = 0
    for i in range(m):
        x += a[i]*b[i]
    if 0 < x + c:
        ans += 1

print (ans)
