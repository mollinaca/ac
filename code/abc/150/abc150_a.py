#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k, x = (int(i) for i in input().split())
if k*500 >= x:
    print ("Yes")
else:
    print ("No")