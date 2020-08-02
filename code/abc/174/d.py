#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
C = input()
C2 = ''
for i in range(len(C)):
    if i == 0:
        pass
    else:
        if C[i-1]+C[i] == 'WR':
            C2 += 'X'
        else:
            C2 += C[i]

ans = 0
for i in range(len(C2)):
    if i == 0:
        if C[i] != 'X':
            pass
        else:



