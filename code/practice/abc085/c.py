#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,Y = map(int,input().split())
for i in range(N+1):
    for j in range(N+1):
        x = i
        y = j
        z = N-(x+y)

        if z < 0:
            break
        if (10000*x + 5000*y + 1000*z) == Y:
            print (x,y,z)
            exit ()
print (-1,-1,-1)
