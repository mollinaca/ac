#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
l = sorted(list(map(int,input().split())))
print (sum(l[0:m]))
