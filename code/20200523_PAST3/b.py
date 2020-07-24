#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m,q = map(int,input().split())

ac_d = {}
for i in range(1,n+1):
    ac_d[i] = []

tokuten_d = {}
for i in range(1,m+1):
    tokuten_d[i] = n

def print_score(x):
    # 参加者 x のその時点でのスコアを出力
    score = 0
    for i in ac_d[x]:
        score += tokuten_d[i]

    print (score)
    return

for i in range(1,q+1):
    q = list(map(int,input().split()))

    if q[0] == 1:
        # スコアを出力
        print_score(q[1])
    else: # q[0] == 2:
        # 問題を解いた
        ac_d[q[1]].append(q[2])
        tokuten_d[q[2]] -= 1
