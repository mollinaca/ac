#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r,d,x = map(int,input().split())
for _ in range(10):
    x = (r*x)-d
    print (x)