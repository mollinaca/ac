#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
ans = 753

for i in range(len(s)-2):
    if abs(753-int(s[i:i+3])) < ans:
        ans = abs(753-int(s[i:i+3]))

print (ans)