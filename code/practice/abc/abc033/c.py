#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = list(input().split("+"))
ans = 0
for kou in s:
    if not "0" in kou:
        ans += 1
print (ans)
