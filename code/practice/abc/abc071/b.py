#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
for x in [chr(i) for i in range(97, 97+26)]:
    if x not in s:
        print (x)
        exit ()
print ("None")
