#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
d = {}
invalid = False
for _ in range(m):
    s,c = map(int,input().split())
    if n != 1 and s == 1 and c == 0:
        invalid = True
    if s in d:
        if d[s] != c:
            invalid = True
    else:
        d[s] = c

if invalid:
    print (-1)
    exit ()

for i in range(1,n+1):
    if i in d:
        print (d[i],end="")
    else:
        if n == 1:
            print (0)
            exit ()
        else:
            print (1,end="") if i == 1 else print (0,end="")
print ()