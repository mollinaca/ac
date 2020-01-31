#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
t = 0
for i in range(len(s)):
    if int(s[i]) == 1:
        t+=1
print (t)