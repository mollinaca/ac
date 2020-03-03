#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(500000)
h,w=map(int,input().split())
l=[list(input()) for _ in range(h)]

def dfs(r,c):
	if not(0<=c<w and 0<=r<h) or l[r][c]=="#":
		return
	if l[r][c]=="g":
		print("Yes")
		exit()
	l[r][c]="#"
	dfs(r+1,c)
	dfs(r-1,c)
	dfs(r,c+1)
	dfs(r,c-1)

for i,y in enumerate(l):
	if "s" in y:
		dfs(i,y.index("s"))
		break
print("No")
