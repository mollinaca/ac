#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
t = input()
ans = 0
for i,j in zip(s,t):
    if i == j:
        ans += 1
print (ans)
