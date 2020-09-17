#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter

n = int(input())
a = list(map(int,input().split()))
a_count = sorted(Counter(a).items(),reverse=True)
f = False

for k,v in a_count:
    if (4 <= v) and (not f):
        print (k**2)
        exit ()
    elif 2 <= v:
        if f:
            print (x*k)
            exit ()
        else:
            x = k
            f = True
    else:
        pass

print (0)
