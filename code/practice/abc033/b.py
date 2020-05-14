#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
city = {}
total = 0
for _ in range(n):
    n,m = input().split()
    city[n] = int(m)
    total += int(m)

for k,v in city.items():
    if v*2 > total:
        print (k)
        exit ()
print ("atcoder")
