#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
N,M,X = map(int,input().split())
C = []
for _ in range(N):
    l = list(map(int,input().split()))
    C.append(l)

tmpl = []
try:
    for i in range(12):
        tmpl.append(C[i][1])
except:
    pass

tmpl2 = []
for i in range(1,len(tmpl)+1):
    for j in itertools.permutations(tmpl, r=i):
        if sum(j) >= X:
            tmpl2.append(sorted(j))

list1 = (set(map(tuple, tmpl2)))
print (list1)

if len(list1) == 0:
    print (-1)
    exit ()
