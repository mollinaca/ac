#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = [1,2,3,4,5,6]
n = n%30

for i in range(n):
    t = i%5
    tmp = l[t]
    l[t] = l[t+1]
    l[t+1] = tmp

print(''.join(map(str, l)))
