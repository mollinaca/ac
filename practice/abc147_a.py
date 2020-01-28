#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i = list(map(int, input().split()))
a=i[0]
b=i[1]
c=i[2]

if a+b+c < 22:
    print ("win")
    exit (0)
print ("bust")
