#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
if a == b:
    for _ in range (a):
        print (a,end="")
    exit (0)
else:
    if a < b:
        for _ in range(b):
            print (a,end="")
    else:
        for _ in range(a):
            print (b,end="")