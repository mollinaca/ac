#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n = int(input())

if n%2 == 0:
    x = -1
else:
    x = 1

ans = 0
R = []
for _ in range(n):
    R.append(int(input()))
R = sorted(R)

for r in R:
    ans += math.pi*r*r*x
    x *= -1
print (ans)
