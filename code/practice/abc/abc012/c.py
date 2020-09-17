#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = 2025-int(input())
for i in range(1,10):
    for j in range(1,10):
        if i*j == x:
            print (i,"x",j)
