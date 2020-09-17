#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
ans = float('inf')

for i in range(min(a),max(a)+1):
    total = 0
    for b in a:
        total += (b-i)**2
    if total <= ans:
        ans = total
print (ans)