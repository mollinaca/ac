#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
t = 0
x = 0
y = 0

def eo (a,b):
    if a%2 == 0 and b%2 == 0:
        return True
    elif a%2 == 1 and b%2 == 1:
        return True
    else:
        return False

for _ in range(n):
    next_t, next_x, next_y = map(int, input().split())
    if next_t - t >= (next_x-x)+(next_y-y) and eo(next_t-t,(next_x-x)+(next_y-y)):
        t = next_t
        x = next_x
        y = next_y
    else:
        print ("No")
        exit (0)

print ("Yes")