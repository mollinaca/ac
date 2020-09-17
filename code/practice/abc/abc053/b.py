#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = list(input())
a = s.index("A")
z = len(s) - s[-1:0:-1].index("Z")
print (z-a)