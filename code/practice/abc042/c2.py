#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(500000)

n,k = map(int,input().split())
D = list(map(int,input().split()))

ans = []
def dfs(p:str):
    if int(p)>=n:
        ans.append(int(p))
        return

    if len(p)>len(str(n))+1:
        return

    for i in range(10):
        if not i in D:
            dfs(p+str(i))

for i in range(10):
    if not i in D:
        dfs(str(i))

print (min(ans))
