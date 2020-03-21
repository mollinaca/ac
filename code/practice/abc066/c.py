#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
ar = list(reversed(a))
b = []
c = []

if len(a)%2 == 0:
    for i in range(len(a)//2):
        b.append(ar[i*2])
        c.append(a[i*2])
else:
    for i in range(-(-(len(a))//2)):
        if i == len(a)//2:
            b.append(ar[(i*2)])
        else:
            b.append(ar[i*2])
            c.append(a[(i*2)+1])

print(' '.join(map(str, b+c)))
