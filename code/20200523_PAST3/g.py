#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**7)

n,x,y = map(int,input().split())
if x < 0 or y < 0:
    p = min(x,y)
else:
    p = 0

x = x-p
y = y-p
print (x,y)

g = [list("."*(x+1)) for i in range(y+1)]
print (g)

g[0][0] = "S"
g[x][y] = "G"

for _ in range(n):
    a,b = map(int,input().split())
    g[a-p][b-p] = "#"

print (g)
