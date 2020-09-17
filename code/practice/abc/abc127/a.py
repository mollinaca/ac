#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = map(int,input().split())
if a <= 5:
    ans = 0
elif (6 <= a) and (a <= 12):
    ans = b//2
else:
    ans = b
print (ans)
