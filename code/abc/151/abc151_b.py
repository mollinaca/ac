#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k,m = map(int, input().split())
l = list(map(int,input().split()))	
a = 0
for value in l:
    a += value
x = ((n*m) - a)
if x <= 0:
    print ("0")
elif x <= k:
    print (x)
else:
    print ("-1")