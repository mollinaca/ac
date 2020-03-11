#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
t = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    p,x = map(int,input().split())
    p = p-1
    total = 0
    for i in range(len(t)):
        if i == p:
            total += x
        else:
            total += t[i]
    print (total)