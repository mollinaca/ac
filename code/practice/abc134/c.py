#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

m = max(A)
c = A.count(m)
if c == 1:
    m2 = sorted(set(A),reverse=True)[1]
    for i in A:
        print (m) if i != m else print(m2)
else:
    for _ in range(n):
        print (m)
