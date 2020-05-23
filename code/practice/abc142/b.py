#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
for i in l:
    if i >= k:
        ans += 1
print (ans)
