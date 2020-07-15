#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,x = map(int,input().split())
d = []
for _ in range(n):
    d.append(int(input()))
print (n + (x - sum(d))//min(d))
