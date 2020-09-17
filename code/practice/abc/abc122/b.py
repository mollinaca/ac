#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()

ans = 0
n = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'T' or s[i] == 'C' or s[i] == 'G':
        n += 1
        if ans < n:
            ans = n
    else:
        n = 0

print (ans)
