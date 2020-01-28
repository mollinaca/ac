#!/usr/bin/env python3
# -*- coding: utf-8 -*-
i = list(map(int, input().split()))
a=i[0]
b=i[1]

if a % 2 == 0 or b % 2 == 0:
    print ("Even")
    exit (0)

print ("Odd")