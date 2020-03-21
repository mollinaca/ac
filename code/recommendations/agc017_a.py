#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,p = map(int,input().split())
a = list(map(int, input().split()))
if all(x%2 == 0 for x in a):
    if p == 0:
        ans = 2**n
    else:
        ans = 0
else:
    ans = 2**(n-1)
print (ans)
