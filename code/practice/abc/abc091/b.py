#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
ds = {}
for _ in range(n):
    s = input()
    if s not in ds.keys():
        ds[s] = 1
    else:
        ds[s] += 1

m = int(input())
dt = {}
for _ in range(m):
    s = input()
    if s not in dt.keys():
        dt[s] = 1
    else:
        dt[s] += 1

ans = 0
for k in ds.keys():
    if k in dt.keys():
        tmp = ds[k] - dt[k]
    else:
        tmp = ds[k]

    if ans < tmp:
        ans = tmp

print (ans)
