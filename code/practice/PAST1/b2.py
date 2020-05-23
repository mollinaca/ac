#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    if i == 0:
        a = int(input())
    else:
        prev_a = a
        a = int(input())
        if prev_a < a:
            print ("up",a-prev_a)
        elif prev_a > a:
            print ("down",prev_a-a)
        else:
            print ("stay")
