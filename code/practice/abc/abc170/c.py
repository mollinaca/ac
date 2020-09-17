#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,n = map(int,input().split())

if n == 0:
    print (x)
    exit ()

p = list(map(int,input().split()))

for i in range(201):
    if not x-i in p:
        print (x-i)
        exit ()
    elif not x+i in p:
        print (x+i)
        exit ()
    else:
        pass

