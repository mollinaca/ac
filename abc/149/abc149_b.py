#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a, b, k = (int(i) for i in input().split())
x=a-k
if x < 0:
    y=b+x
    if y < 0:
        print ("0 0")
        exit (0)
    print("0", y)
    exit (0)
print (x, b)
