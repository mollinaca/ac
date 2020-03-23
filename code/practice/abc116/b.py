#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = []
l.append(int(input()))

def next(i:int):
    if l[i-1]%2 == 0:
        return l[i-1]//2
    else:
        return (3*l[i-1])+1

i = 0
while True:
    i += 1
    if next(i) in l:
        print (i+1)
        exit ()
    else:
        l.append(next(i))