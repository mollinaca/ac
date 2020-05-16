#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c,d = map(int,input().split())
if a+b > c+d:
    print ("Left") 
elif a+b == c+d:
    print ("Balanced")
else: #a+b < c+d
    print ("Right")
