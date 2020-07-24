#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,r,n = map(int,input().split())

if a != 1 and r != 1 and n != 1 and 10000 < len(str(a))+len(str(r))*(n-1):
    print ("large")
else:
    x = a*(r**(n-1))
    if x <= 10**9:
        print (int(x))
    else:
        print ("large")
