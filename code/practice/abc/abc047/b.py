#!/usr/bin/env python3
# -*- coding: utf-8 -*-
W,H,N = map(int,input().split())
X0 = 0
X = W
Y0 = 0
Y = H
for _ in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        X0 = max(X0,x)
    elif a == 2:
        X = min(X,x)
    elif a == 3:
        Y0 = max(Y0,y)
    else: # a == 4
        Y = min(Y,y)

if X0 >= X or Y0 >= Y:
    print (0)
else:
    print ((X-X0)*(Y-Y0))
