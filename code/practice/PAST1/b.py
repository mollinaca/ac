#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    a = int(input())
    if i == 0:
        prev_a = a
    else:
        if prev_a == a:
            print ("stay")
        elif prev_a > a:
            print ("down",prev_a-a)
        else:
            print ("up",a-prev_a)
        prev_a = a
