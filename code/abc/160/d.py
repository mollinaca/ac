#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,x,y = map(int,input().split())
d = {}
for i in range(1,n+1):
    if i == 1:
        d[i]=[2]
    elif i == n:
        pass
#        d[i]=[i-1]
    else:
#        d[i]=[i-1,i+1]
        d[i]=[i+1]
    if i == x:
        d[i].append(y)
    elif i == y:
        pass
#        d[i].append(x)

print (d)
#for i in range(1,n):
#    c=0
#    for k in d.keys():

