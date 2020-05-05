#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
ans = float('inf')
for _ in range(n):
    x = int(input())
    ans = min(x,ans)
print (ans)
