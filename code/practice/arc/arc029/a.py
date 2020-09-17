#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
niku = []
for _ in range(n):
    niku.append(int(input()))
niku.sort()

if n == 1:
    print (niku[0])
elif n == 2:
    print (niku[1])
elif n == 3:
    print (max(niku[0]+niku[1],niku[2]))
else: # n == 4
    print(min(max(niku[3],niku[0]+niku[1]+niku[2]),max(niku[3]+niku[0],niku[1]+niku[2])))
