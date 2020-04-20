#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = sorted(list(map(int,input().split())))
d = {}

for i in range(min(a)-1,max(a)+2):
    d[i] = 0

for v in a:
    d[v] += 1

ans = 0
for i in range(min(a),max(a)+1):
    tmp = d[i-1]+d[i]+d[i+1]
    if ans < tmp:
        ans = tmp
print (ans)
