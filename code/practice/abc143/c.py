#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
s = input()
ans = 0
for i in range(n):
    if i == 0:
        pass
    else:
        if s[i] != s[i-1]:
            ans += 1
print (ans+1)
