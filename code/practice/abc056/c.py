#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = int(input())
i = 0
while True:
    if i*(i+1)//2 >= x:
        print (i)
        exit ()
    i += 1
