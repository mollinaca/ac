#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,a,b = map(int,input().split())

def total (x:int):
    total = 0
    while True:
        if x == 0:
            return total
        else:
            total += x%10
            x = x//10

ans = 0
for i in range(0,n+1):
    t = total(i)
    if a <= t and t <= b:
        ans += i

print (ans)
