#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque

N = int(input())
S = input()
s = deque(S)
d = deque()
d.append('b')

if d == s:
    print (0)
    exit ()

i = 0
while True:
    if len(d) > N:
        print (-1)
        exit ()
    
    d.appendleft('a')
    d.append('c')
    if d == s:
        print ((i*3)+1)
        exit ()
    
    d.appendleft('c')
    d.append('a')
    if d == s:
        print ((i*3)+2)
        exit ()

    d.appendleft('b')
    d.append('b')
    if d == s:
        print (i*3+3)
        exit ()
    
    i += 1
