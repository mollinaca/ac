#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
n = int(input())
A = list(map(int,input().split()))
c = Counter(A)
ans = 0
for k,v in c.items():
    if v < k:
        ans += v
    else:
        ans += v-k
print (ans)
