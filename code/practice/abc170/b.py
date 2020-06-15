#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,y = map(int,input().split())

for i in range(x+1):
    j = x-i
    if (i*2)+(j*4) == y:
        print ("Yes")
        exit ()
else:
    print ("No")
