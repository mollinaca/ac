#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m,x = map(int,input().split())
C = []
for _ in range(n):
    l = list(map(int,input().split()))
    C.append(l)

l = []
for i in range(n):
    l.append(C[i][1])

print (l)

for i in range(2**m):
    ans_l = []
    print (f"{i=}")
    for j in range(n):
        print (f"{j=}")
        if ((i>>j)&1):
            ans_l.append(l[i])

print (ans_l)
