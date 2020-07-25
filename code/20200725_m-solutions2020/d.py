#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))

m = 1000
k = 0

for i in range(n):
    if i == n-1: # 最後ながら全部売る
        m = m + A[i]*k
    elif A[i] <= m and A[i] < A[i+1]: #お金あって明日上がるなら買う
        k = m//A[i]
        m = m - A[i]*k
    elif 0 < k and A[i+1] < A[i]: #株があって明日下がるなら売る
        m = m + A[i]*k
        k = 0
    else:
        pass

print (m)
