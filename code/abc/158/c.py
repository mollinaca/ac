#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a,b = map(int,input().split())
for i in range(100000):
    if (math.floor(i*0.08) == a) and (math.floor(i*0.1) == b):
        print (i)
        exit ()
else:
    print (-1)