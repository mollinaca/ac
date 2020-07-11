#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

ans = [0 for _ in range(10050)]
for i in range(1,105):
    for j in range(1,105):
        for k in range(1,105):
            v = i**2 + j**2 + k**2 + i*j + j*k + k*i
            if v < 10050:
                ans[v] += 1

for i in range(n):
    print (ans[i+1])
