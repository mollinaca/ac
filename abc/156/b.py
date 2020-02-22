#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int, input().split())
count = 0
while True:
    n = n//k
    count += 1
    if n == 0:
        print (count)
        exit (0)
