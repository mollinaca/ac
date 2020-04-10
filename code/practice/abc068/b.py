#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
if 64 <= n:
    print (64)
elif 32 <= n and n < 64:
    print (32)
elif 16 <= n and n < 32:
    print (16)
elif 8 <= n and n < 16:
    print (8)
elif 4 <= n and n < 8:
    print (4)
elif 2 <= n and n < 4:
    print (2)
else:
    print (1)
