#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
t,a = map(int,input().split())
H = list(map(int,input().split()))
x = float('inf')
for i in range(len(H)):
    tmp = t - H[i]*0.006
    tmp2 = abs(a-tmp)
    if tmp2 < x:
        ans = i+1
        x = tmp2

print (ans)
