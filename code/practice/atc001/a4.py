#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

stack = [[sx,sy]] # スタート位置をまずstackに詰む
visited = [[0 for i in range(w)] for j in range(h)] # 探索済みリストを初期化する
visited[sx][sy] = 1 # 探索済みリストにスタート位置を積む

while stack:
    x,y = stack.pop() # stackから先頭の要素を pop する

    nx,ny = x-1, y # 現在位置を移動する
    if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and grid[nx][ny] != '#': #移動先が、範囲内で、かつ未探索で、かつ '#' でない場合
        visited[nx][ny] = 1 # 移動先を移動済みにする
        stack.append([nx,ny]) # 移動先をstackの先頭に push する

    nx,ny = x, y-1 # 現在位置を移動する
    if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and grid[nx][ny] != '#': #移動先が、範囲内で、かつ未探索で、かつ '#' でない場合
        visited[nx][ny] = 1 # 移動先を移動済みにする
        stack.append([nx,ny]) # 移動先をstackの先頭に push する

    nx,ny = x+1, y # 現在位置を移動する
    if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and grid[nx][ny] != '#': #移動先が、範囲内で、かつ未探索で、かつ '#' でない場合
        visited[nx][ny] = 1 # 移動先を移動済みにする
        stack.append([nx,ny]) # 移動先をstackの先頭に push する

    nx,ny = x, y+1 # 現在位置を移動する
    if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and grid[nx][ny] != '#': #移動先が、範囲内で、かつ未探索で、かつ '#' でない場合
        visited[nx][ny] = 1 # 移動先を移動済みにする
        stack.append([nx,ny]) # 移動先をstackの先頭に push する

    if visited[gx][gy] == 1: # ゴール位置が移動済みになればクリア
        print("Yes")
        exit ()

print ("No")
