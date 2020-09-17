#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = sorted(list(map(int,input().split())),reverse=True)
k = int(input())
print (l[0]*(2**k)+sum(l[1:]))
