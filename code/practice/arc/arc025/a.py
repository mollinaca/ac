#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = list(map(int,input().split()))
j = list(map(int,input().split()))

ans = 0
for a,b in zip(d,j):
    ans += max(a,b)

print (ans)
