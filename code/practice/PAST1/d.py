#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

if len(A) == len(set(A)):
    print ("Correct")
else:
    c = Counter(A)

    # 重複キー
    dup_key = max(c, key=c.get)

    # 紛失キー
    C = []
    for i in range(1,n+1):
        C.append(i)
    lost_key = list(set(C) - set(A))[0]

    print (dup_key, lost_key)
