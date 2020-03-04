#!/usr/bin/env python3
# -*- coding: utf-8 -*-
m,n = map(int,input().split())
s = []
for _ in range(m):
    s.append(input())
s.sort()
print(''.join(map(str, s)))
