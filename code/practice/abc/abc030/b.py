#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
n = n%12
n = n*30 + m*0.5
m = m*6
if n > m:
    ans = n-m
else:
    ans = m-n
if ans > 180:
    ans = 360 -ans
print (ans)
