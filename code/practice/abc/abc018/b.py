#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
n = int(input())

for _ in range(n):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    s = s[:l]+''.join(reversed(list(s[l:r+1])))+s[r+1:]
print(s)
