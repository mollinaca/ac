#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
total = 0
for i in a:
    j = 0
    while True:
        if i-j == 1 or i-j == 3 or ((i-j)-1)%6 == 0 or ((i-j)-3)%6 == 0:
            total += j
            break
        j += 1
print (total)
