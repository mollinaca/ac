#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
yama = []
for _ in range(n):
    # 縦N、横2N-1 の山
    yama.append(list(input()))

def yamakuzushi (a:int, b:int):
    # aが横、bが縦
    # 入力された a,b は 'x' になっている場所で、上3箇所のいずれかに '#' があれば 'X' に置き換える
    if b-1 < 0: # 一個上の山が存在しなければ終わり
        return 0

    if 0 <= b-1: # 一個上の山が存在する
        if 0 <= a-1: #　左側要素が存在すれば
            if yama[b-1][a-1] == "#":
                yama[b-1][a-1] = "X"

        if yama[b-1][a] == "#": # ちょうど一個上は必ずある
            yama[b-1][a] = "X"

        if a+1 < (2*n)-1: # 右側要素が存在すれば
            if yama[b-1][a+1] == "#":
                yama[b-1][a+1] = "X"

# 下から探索していく
for i in range(n-1,-1,-1): #iは縦、下から上へ
    yama_line = yama[i]
    for j in range(len(yama_line)): #jは横、左から右へ
        if yama_line[j] == "X":
            yamakuzushi (j,i)

for yama_line in yama:
    print(''.join(map(str, yama_line)))
