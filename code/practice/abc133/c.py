#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L,R = map(int,input().split())
ans = 2019

for i in range(L,R+1):
    for j in range(L,R+1):
        if i == j:
            pass
        else:
            x = (i*j)%2019
            if x < ans:
                ans = x
            
            if x == 0:
                print (x)
                exit ()
print (ans)
