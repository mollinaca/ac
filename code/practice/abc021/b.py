#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a,b = map(int,input().split())
k = int(input())
p = list(map(int,input().split()))
print ("NO") if len(p) != len(set(p)) or ((a in p) or (b in p)) else print ("YES")
