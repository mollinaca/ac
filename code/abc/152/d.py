#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
max_len=10**(len(str(n))-1)
print (max_len)
count=0

for a in range(1,n+1):
    print (a)

    for i in range(max_len):
        print (i)
