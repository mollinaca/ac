#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
n = len(s)

def j(x:str):
    for i in range(len(x)//2):
        if x[i] != x[-(i+1)]:
            return False
    return True

if not j(s):
    print ("No")
    exit ()

if not j(s[0:((n-1)//2)]):
    print ("No")
    exit ()

if not j(s[((n+3)//2)-1::]):
    print ("No")
    exit ()

print ("Yes")
