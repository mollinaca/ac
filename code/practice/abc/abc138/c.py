#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
v = sorted(list(map(int,input().split())))
ans = (v.pop(0)+v.pop(0))/2

if v:
    for i in v:
        ans = (ans+i)/2

print (ans)
