#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = {}
a = list(map(int,input().split()))
for i in a:
    if not i in A:
        A[i] = 1
    else:
        A[i] += 1

s = 0
for k,v in A.items():
    s += k*v

Q = int(input())
for _ in range(Q):
    b,c = map(int,input().split())
    if b in A:
        s = s-(b-c)*A[b]
        if not c in A:
            A[c] = A[b]
        else:
            A[c] += A[b]
        A[b] = 0

    print (s)
