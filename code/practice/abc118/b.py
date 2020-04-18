#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
ans = []
l = []
for i in range(n):
    if i == 0:
        ans = list(map(int,input().split()))
        ans.pop(0)
    else:
        l = list(map(int,input().split()))
        l.pop(0)
        ans = set(ans) & set(l)
print (len(ans))
