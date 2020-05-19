#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 再帰による dfs 実装
import sys
sys.setrecursionlimit(500000)
h,w = map(int,input().split())

grid = []
for _ in range(h):
    l = list(input())
    grid.append(l)

def dfs (a:int,b:int):
    # 移動先のポジションが範囲外なら終了
    if not (0<=a<h and 0<=b<w):
        return
    # 移動先のポジションが "#" なら終了
    if grid[a][b] == "#":
        return

    # 移動先がゴールなら終了
    if grid[a][b] == "g":
        print ("Yes")
        exit ()

    # 現在地を探索済み（→2度と訪れない）ようにして、dfsを続ける
    grid[a][b] = "#"
    dfs(a-1,b)
    dfs(a+1,b)
    dfs(a,b-1)
    dfs(a,b+1)

    return

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "s":
            dfs(i,j)
            break

print ("No")
