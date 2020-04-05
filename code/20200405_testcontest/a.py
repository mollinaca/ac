#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S,L,R = map(int,input().split())
if L <= S and S <= R:
    print (S)
elif abs(S-L) < abs(S-R):
    print (L)
else:
    print (R)
