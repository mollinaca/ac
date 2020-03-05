#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,a,b=map(int, input().split())
wa2=0

for i in range (1,n+1):
    wa1 = sum(list(map(int, str(i))))
    if wa1 >= a and wa1 <= b:
        wa2+=i
print (wa2)