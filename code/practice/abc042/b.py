#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,l = map(int,input().split())
s = []
for _ in range(n):
    s.append(input())
s = sorted(s)
print(''.join(map(str, s)))
