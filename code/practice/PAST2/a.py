#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S,T = input().split()

if 'B' in S:
    s = -1*int(S[1])
else:
    s = int(S[0])

if 'B' in T:
    t = -1*int(T[1])
else:
    t = int(T[0])

if ('B' in S and 'F' in T) or ('B' in T and 'F' in S):
    print (abs(t-s)-1)
else:
    print (abs(t-s))
