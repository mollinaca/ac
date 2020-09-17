#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect
n = int(input())
l = sorted(list(map(int,input().split())))

ans = 0
for i in range(n-1,1,-1):
    for j in range(i-1,0,-1):
        x = j - bisect.bisect(l,l[i]-l[j])
        if x>0:
            ans += x

print (ans)
