#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = sorted(list(map(int,input().split())))
ans = 1
for i in A:
    ans = ans*i
    if 10**18 < ans:
        print (-1)
        exit ()
print (ans)
