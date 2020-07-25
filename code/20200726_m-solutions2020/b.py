#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c, = map(int,input().split())
k = int(input())

while 0 <= k:
    if a < b < c:
        print ("Yes")
        exit ()
    elif a >= b:
        b *= 2
    elif b >= c:
        c *= 2
    else:
        pass
    k -= 1
print ("No")
