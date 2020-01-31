#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,y=map(int, input().split())
for a in range(n+1):
    if 10000*a > y:
        break
    for b in range(n+1-a):
        c = n - (a+b)
        if c < 0:
            break
        if (10000*a) + (5000*b) + (1000*c) == y:
            print (a,b,c)
            exit (0)
print ("-1 -1 -1")
