#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
import sys
from collections import deque
sys.setrecursionlimit(500000)
h,w=map(int,input().split())
l=[list(input()) for _ in range(h)]

#print (l)

# 準備
st = deque() #深さ有線探索用のstack
check_l = [list(0) for _ in range(h)] 

def dfs(x:int,y:int):
    if not(0<=x<w and 0<=y<h) or l[x][y]=="#":
        return 
    if l[x][y] == "g":
        print ("Yes")
        exit ()
        