#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
total = 0
for i in range(1,n+1):
    if i%3 == 0 or i%5 == 0:
        pass
    else:
        total += i
print (total)
