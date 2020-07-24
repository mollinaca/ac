#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m,q = map(int,input().split())

graph = {}
for i in range(1,n+1):
    graph[i] = []

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

color = {}
l = list(map(int,input().split()))
for i in range(len(l)):
    i = i
    color[i+1] = l[i]

def q1 (x:int):
    print (color[x])
    # スプリンクラー処理
    for target_node in graph[x]:
        color[target_node] = color[x]

    return

def q2 (x:int,y:int):
    print (color[x])
    color[x] = y
    return

for _ in range(q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        q1 (q[1])
    else: #q[0] == 2:
        q2 (q[1],q[2])
