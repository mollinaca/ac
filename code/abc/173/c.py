#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

h,w,k = map(int,input().split())
grid = [list(input()) for i in range(h)]

b = 0
for l in grid:
    b += l.count("#")
z = b - k
print (z)

ans = 0

def judge(X:int,Y:int):
    a = 0
    for x in itertools.combinations([i for i in range(w)],X):
        for y in itertools.combinations([i for i in range(h)],Y):
            print(x,y)

for i in range(z+1):
    for j in range(z+1):
        if z < i+j:
            break
        else:
            # h,w から除外してみる本数候補
            print (i,j)
            judge(i,j)
