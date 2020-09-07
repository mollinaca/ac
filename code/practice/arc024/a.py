#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l,r = map(int,input().split())
L = list(map(int,input().split()))
R = list(map(int,input().split()))
Ld = {}
Rd = {}

for x in L:
    if not x in Ld:
        Ld[x] = 1
    else:
        Ld[x] += 1

for x in R:
    if not x in Rd:
        Rd[x] = 1
    else:
        Rd[x] += 1

ans = 0
for k,v in Ld.items():
    if k in Rd:
        ans += min(Ld[k],Rd[k])

print (ans)
