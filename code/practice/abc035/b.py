#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = input()
T = int(input())

p = [0,0]
c = 0
for s in S:
    if s == '?':
        c += 1
    elif s == 'L':
        p[0] -= 1
    elif s == 'R':
        p[0] += 1
    elif s == 'U':
        p[1] += 1
    else: #s == 'D'
        p[1] -= 1

d = abs(p[0]) + abs(p[1])
if T == 1:
    print (d+c) 
else: # T == 2
    if d-c < 0:
        if (c-d)%2 == 0:
            print (0)
        else:
            print (1)
    else:
        print (d-c)
