#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
m=0
for i in a:
    if i >= m:
        m = i

print (m)