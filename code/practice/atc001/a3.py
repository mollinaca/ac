#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# stack による dfs 実装
# ref: https://nashidos.hatenablog.com/entry/2020/01/04/234842
#import sys
#sys.setrecursionlimit(500000)
#import collections
h,w = map(int,input().split())

grid = []
for _ in range(h):
    l = list(input())
    grid.append(l)

for i in range(h):
    for j in range(w):
        if grid[i][j] == "s": # スタート位置を取得
            sx,sy = i,j
        elif grid[i][j] == "g": # ゴール位置を取得
            gx,gy = i,j
        else:
            pass
dx_dy = [[1,0],[0,1],[-1,0],[0,-1]] # 計算用

stack = [[sx,sy]] # スタート位置をまずstackに詰む
visited = [[0 for i in range(w)]for j in range(h)] # 探索済みリストを初期化する
visited[sx][sy] = 1 # 探索済みリストにスタート位置を積む

while stack:
    x,y = stack.pop() # stackから先頭の要素を pop する
    for i in range(4):
        nx,ny = x+dx_dy[i][0], y+dx_dy[i][1] # 現在位置を移動する。forで4回回る（4方に動く）
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and grid[nx][ny] != '#': #移動先が、範囲内で、かつ未探索で、かつ '#' でない場合
#            print (stack,visited,nx,ny)
            visited[nx][ny] = 1 # 移動先を移動済みにする
            stack.append([nx,ny]) # 移動先をstackの先頭に push する

    if visited[gx][gy] == 1: # ゴール位置が移動済みになればクリア
        print("Yes")
        exit ()

print ("No")
