#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
print ("Yes") if max(l) < sum(l)-max(l) else print ("No")
