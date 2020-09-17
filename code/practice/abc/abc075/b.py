#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,w = map(int,input().split())
grid = []

for _ in range(h):
    l = list(input())
    grid.append(l)

def search(a,b):
    if grid[a][b] == "#":
        return "#"

    mine = 0

    if 0 <= a-1 and 0 <= b-1:
        if grid[a-1][b-1] == "#":
            mine += 1

    if 0 <= a-1:
        try:
            if grid[a-1][b] == "#":
                mine += 1
        except:
            pass

        try:
            if grid[a-1][b+1] == "#":
                mine += 1
        except:
            pass

    if 0 <= b-1:
        if grid[a][b-1] == "#":
                mine += 1

        try:
            if grid[a+1][b-1] == "#":
                mine += 1
        except:
            pass

    try:
        if grid[a][b+1] == "#":
            mine += 1
    except:
        pass


    try:
        if grid[a+1][b] == "#":
            mine += 1
    except:
        pass

    try:
        if grid[a+1][b+1] == "#":
            mine += 1
    except:
        pass

    return mine

ans = []
for i in range(h):
    l = []
    for j in range(w):
        l.append(search(i,j))
    ans.append(l)

for i in range(h):
    print(''.join(map(str, ans[i])))
