#!/usr/bin/env python3
# -*- coding: utf-8 -*-
m,n,x = map(int,input().split())
a = list(map(int,input().split()))
i = len([i for i in a if i < x])
j = len([i for i in a if i > x])
print (i) if i < j else print (j)
