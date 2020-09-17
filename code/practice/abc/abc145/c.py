#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import math
n = int(input())
town = []
for _ in range(n):
    l = list(map(int,input().split()))
    town.append(l)

l = []
for i in range(n):
    l.append(i)

def calc (a,b,c,d):
    return math.sqrt(((a-b)**2)+((c-d)**2))

total = 0
for v in itertools.permutations(l):
    for i in range(len(v)):
        if i == n-1:
            pass
        else:
            total += calc(town[v[i]][0],town[v[i+1]][0],town[v[i]][1],town[v[i+1]][1])

print (total/math.factorial(n))
