#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = list(input())
ans = "Yes"
for i in range(len(s)):
    if i%2 == 0: #奇数文字目
        if s[i] == 'L':
            ans = "No"
    else:
        if s[i] == 'R':
            ans = "No"

print (ans)
