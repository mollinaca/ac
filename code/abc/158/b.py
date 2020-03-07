#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,a,b = map(int,input().split())
x = -(-n//(a+b))
total = (a+b)*(x-1)
total_a = a*(x-1)
if n - total >= a:
    print (total_a + a)
else:
    print (total_a + (n-total))