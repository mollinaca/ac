#!/usr/bin/env python3
# -*- coding: utf-8 -*-
grid = []
for _ in range(3):
    array = list(map(int, input().strip().split()))
    grid.append(array)

def judge():
    for i in range(3):
        if grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] == 0:
            return True
        if grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] == 0:
            return True
    if grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] == 0:
        return True
    if grid[0][2] == 0 and grid[1][1] == 0 and grid[2][0] == 0:
        return True
    return False

n = int(input())
ans = "No"
for _ in range(n):
    b = int(input())
    for i in range(3):
        if b in grid[i]:
            grid[i][grid[i].index(b)] = 0
    if judge():
        ans = "Yes"
#    print (grid)

print (ans)