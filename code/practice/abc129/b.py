#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
w = list(map(int, input().split()))
delta = max(w)
for i in range(n):
    c = abs( sum(w[0:i]) - sum(w[i:n]) )
    if c <= delta:
        delta = c
print (delta)