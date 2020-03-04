#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int, input().split())
d = list(input().split())
for i in range(n,100000):
    for j in d:
        if j in str(i):
            break
    else:
        print (i)
        exit ()