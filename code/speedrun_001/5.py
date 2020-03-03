#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
for i in range(len(a)):
    if a[i] == 1:
        print (i+1)