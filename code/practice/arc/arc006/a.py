#!/usr/bin/env python3
# -*- coding: utf-8 -*-
E = set(map(int,input().split()))
B = int(input())
L = set(map(int,input().split()))

if len(E&L) == 6:
    print (1)
elif len(E&L) == 5:
    if L-E == {B}:
        print (2)
    else:
        print (3)
elif len(E&L) == 4:
    print (4)
elif len(E&L) == 3:
    print (5)
else:
    print (0)
