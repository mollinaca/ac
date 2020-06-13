#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
s = input()

if s.count('-') == 1:
    x,y = s.split('-')
    if x.isdigit and y.isdigit and len(x) == n and len(y) == m:
        print ("Yes")
        exit ()

print ("No")
