#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
graph_d = {}
ans_l = []
ans_d = {}
for i in range(1,n+1):
    graph_d[i] = []

for _ in range(m):
    a,b = map(int,input().split())
    graph_d[a].append(b)
    graph_d[b].append(a)

for i in range(1,len(graph_d)+1):
    if 1 in graph_d[i]:
        ans_d[i] = 1
        ans_l.append(i)

for k,v in graph_d.items():
    if k == 1 or k in ans_l:
        continue

    for j in ans_l:
        if j in v:
            ans_d[k] = j

if len(ans_d) == n-1:
    print ("Yes")
    for i in range(2,n+1):
        print (ans_d[i])
else:
    print ("No")
