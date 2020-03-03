#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
if len(l) == len(set(l)):
    print ("YES")
else:
    print ("NO")