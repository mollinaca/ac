#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import floor
a,b,n = map(int,input().split())
x = min(b-1,n)
print (floor((a*x/b) - a*(floor(x/b))))
