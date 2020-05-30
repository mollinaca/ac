#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,x = map(int,input().split())
L = list(map(int,input().split()))

ans = 1
r = 0
for l in L:
    r += l
    if x < r:
        print (ans)
        exit ()
    else:
        ans += 1
print (ans)
