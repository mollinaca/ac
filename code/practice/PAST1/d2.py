#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
n = int(input())
C = [i for i in range(1,n+1)]
A = []
for _ in range(n):
    A.append(int(input()))
A.sort()

# 重複
c = Counter(A)
if c.most_common()[0][1] == 2:
    duble = c.most_common()[0][0]
else:
    print ("Correct")
    exit ()

# 抜け
s = set(C)-set(A)

print (duble,list(s)[0])
