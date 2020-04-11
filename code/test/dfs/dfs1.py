#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://qiita.com/takayg1/items/7008e4c9584e42ae13c7
# 行きがけ
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
#    print (u,k,v)
    for i in v:
            graph[u].append(i)
            # graph[i].append(u) # 無向グラフ
# print (graph)

time = 0
arrive_time = [-1] * (N+1)

def dfs(v):
    global time
    time += 1
    stack = [v]
    arrive_time[v] = time
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if arrive_time[w] < 0:
                time += 1
                arrive_time[w] = time
                stack.append(w) 
        else:
            stack.pop()          
    return arrive_time

for i in range(N):
    if arrive_time[i + 1] < 0:
        ans = dfs(i + 1)

for j in range(N):
    temp = [j + 1, ans[j + 1]]
    print(* temp)
