#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
ans = float('inf')
for i in range(len(s)-2):
    x = abs(753-int(s[i:i+3]))
    if x < ans:
        ans = x
print (ans)
