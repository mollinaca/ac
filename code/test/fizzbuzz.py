#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
for i in range(1,n+1):
    if i%15 == 0:
        print ("FIZZBUZZ")
    elif i%3 == 0:
        print ("FIZZ")
    elif i%5 == 0:
        print ("BUZZ")
    else:
        print (i)