#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
s = str(input())
count = 0
for i in range(0,n):
    if s[i] == "A":
        if i+2 <= n-1:
            if s[i+1] == "B" and s[i+2] == "C":
                count += 1
print (count)