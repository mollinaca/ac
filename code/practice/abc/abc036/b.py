#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
grid = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(n-1,-1,-1):
        print (grid[j][i], end="")
    print ()
