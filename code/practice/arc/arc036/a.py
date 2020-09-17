#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
for i in range(1,n+1):
    if i == 1:
        t1 = int(input())
    elif i == 2:
        t2 = int(input())
    else:
        t3 = int(input())
        if t1+t2+t3 < k:
            print (i)
            exit ()
        else:
            t1 = t2
            t2 = t3

print (-1)
