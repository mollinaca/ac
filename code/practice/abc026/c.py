#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
d = {} # 各社員の上司リスト、1の人は0が入る
l = [] # 上司そのもののリスト
d2 = {} # 各社員給料リスト、最初は全員1、これの d2[1] の最後の状態が解

for i in range(1,n+1):
    if i == 1:
        d[i] = 0
        d2[i] = 1
    else:
        x = int(input())
        d[i] = x
        l.append(x)
        d2[i] = 1
l = sorted(list(set(l)),reverse=True)

for boss in l:
    tmpl = []
    for k,v in d.items():
        if v == boss:
            tmpl.append(d2[k])
    d2[boss] = max(tmpl)+min(tmpl)+1

print (d2[1])
