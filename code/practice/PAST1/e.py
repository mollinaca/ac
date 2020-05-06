#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,q = map(int,input().split())
f = []

# init
for _ in range(n):
    l = ['N' for l in range(n)]
    f.append(l)

def follow (a:int,b:int):
    """
    a が b をフォローする
    """
    f[a-1][b-1] = 'Y'

def followback (a:int):
    """
    a が a をフォローしてる人をフォローし返す
    """
    for i in range(n):
        if i == a-1:
            pass
        else:
            l = f[i]
            if l[a-1] == 'Y':
                follow (a,i+1)

def followfollow (a:int):
    """
    a が 自分がフォローしてる人がフォローしてる人をフォローする
    """
    # a がフォローしてるリスト
    al = []
    l = f[a-1]
    for i in range(n):
        if l[i] == 'Y':
            al.append(i+1)

    # フォローしてる人がフォローしてる人をフォローしていく
    for i in al:
        for j in range(n):
            if f[i-1][j] == 'Y':
                follow (a,j+1)

def display (f:list):
    for i in range(len(f)):
        print(''.join(map(str, f[i])))

# 処理
for _ in range(q):
    S = list(input().split())

    if S[0] == '1':
        follow (int(S[1]),int(S[2]))
    elif S[0] == '2':
        # フォロー全返し
        followback (int(S[1]))
    elif S[0] == '3':
        # フォローフォロー
        followfollow (int(S[1]))

#    display (f)

display (f)
