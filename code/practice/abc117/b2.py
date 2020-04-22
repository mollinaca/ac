#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))

for i in l:
    if i < sum(l)-i:
        pass
    else:
        print ("No")
        exit ()
print ("Yes")
