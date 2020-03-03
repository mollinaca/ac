#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
for i in range(len(a)):
    print (a[i], end="")
    if not i+1 == len(a):
        print (",",end="")