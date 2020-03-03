#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
x = list(map(int, input().split()))
x.sort()
score = []
for a in range(min(x),max(x)+1):
    s = 0
    for b in x:
        s += (b-a)**2
    score.append(s)
print (min(score))
