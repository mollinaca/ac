#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
H = list(map(int,input().split()))

ans = 0
c = 0
for i in range(len(H)):
    if i == len(H)-1:
        print (ans) if c < ans else print (c)
    else:
        if H[i+1] <= H[i]:
            c += 1
        else:
            if ans < c:
                ans = c
            c = 0

