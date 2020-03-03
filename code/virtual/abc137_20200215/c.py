#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = {}
count = 0

for i in range(n):
    s = ''.join(sorted(input()))
    if i == 0:
        l[s] = 1
        continue

    # ハッシュを確認し、登場していればcountを+l[s]、していなければハッシュに追加する
    if s in l:
        count+=l[s]
        l[s] += 1
    else:
        l[s] = 1

print (count)
