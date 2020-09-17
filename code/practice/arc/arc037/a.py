#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
ans = 0
for i in l:
    ans += max(0,80-i)
print (ans)
