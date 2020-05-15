#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = []
t = x = y = 0
for _ in range(n):
    a,b,c = map(int,input().split())
    t_delta = a - t
    x_delta = abs(b - x)
    y_delta = abs(c - y)

    if (x_delta+y_delta <= t_delta) and (t_delta%2 == (x_delta+y_delta)%2):
            pass
    else:
        print ("No")
        exit ()

    t = a
    x = b
    y = c

print ("Yes")
