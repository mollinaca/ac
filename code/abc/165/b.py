#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import floor
x = int(input())
y = 100
i = 0
while True:
    i += 1
    risoku = floor(y*(1/100))
    y = y+risoku

    if y >= x:
        print (i)
        exit ()
