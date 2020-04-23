#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/arc012/tasks/arc012_2
n,va,vb,l = map(int,input().split())
for _ in range(n):
    t = l/va
    l -= (va-vb)*t
print (l)
