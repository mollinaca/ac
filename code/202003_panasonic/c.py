#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())
d = c - a - b
print ("Yes") if d > 0 and d**2 > 4*a*b else print ("No")