#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
score = []
for _ in range(n):
    l = list(map(int,input().split()))
    score.append(sum(l[0:4])+l[4]*(110/900))
print (max(score))
