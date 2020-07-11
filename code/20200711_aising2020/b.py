#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
ans = 0
for i in range(len(l)):
    if ((i+1)%2 == 1) and (l[i]%2 == 1):
        ans += 1
print (ans)
