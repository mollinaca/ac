#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
n = int(input())
a = list(map(int, input().split()))
l = [0]*n
ans = 0

for k,v in collections.Counter(a).items():
    l[k-1] = v
    ans += v*(v-1)//2

for i in range(n):
    print (ans-l[a[i]-1]+1)