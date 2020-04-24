#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,S,T = map(int,input().split())
c = 0

W = int(input())
if S <= W and W <= T:
    c += 1

for _ in range(N-1):
    a = int(input())
    W = W+a
    if S <= W and W <= T:
        c += 1

print (c)
