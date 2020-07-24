#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
t = input()

ans = "different"

if s.lower() == t.lower():
    ans = "case-insensitive"

for i in range(len(s)):
    if not s[i] == t[i]:
        break
else:
    ans = "same"

print (ans)
