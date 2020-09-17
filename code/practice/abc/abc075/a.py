#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())
if a == b:
    print (c)
elif a == c:
    print (b)
else: #b == c
    print (a)
