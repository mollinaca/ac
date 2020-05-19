#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(500000)

n = int(input())

def dfs(s:str):
    # 文字列が長さに達してたら出力してreturnする
    if len(s) == n:
        print (s)
        return

    dfs (s+"a")
    dfs (s+"b")
    dfs (s+"c")

for a in ["a","b","c"]:
    dfs (a)
