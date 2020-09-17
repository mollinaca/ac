#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

def dfs (n:int, c:int):
    print (n,c)
    if c <= 100 and n == 0: #100回以内に0にできた
        print ("YES")
        exit ()

    if c == 100: #100回目に到達したので、101回目の操作はできない
        return

    if n-1 != ng1 and n-1 != ng2 and n-1 != ng3:
        dfs (n-1,c+1)
    elif n-2 != ng1 and n-2 != ng2 and n-2 != ng3:
        dfs (n-2,c+1)
    elif n-3 != ng1 and n-3 != ng2 and n-3 != ng3:
        dfs (n-3,c+1)
    else: # どれを引いても ng1/ng2/ng3 になる
        return

if n == ng1 or n == ng2 or n == ng3:
    print ("NO")
else:
    dfs (n,0)
    print ("NO")
