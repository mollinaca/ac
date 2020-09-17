#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
k = []
s = []
for _ in range(m):
    l = list(map(int,input().split()))
    k.append(l[0])
    s.append(l[1:])
p = list(map(int,input().split()))

# bit全探索
ans = 0
for i in range(2**n):
    c = 0

    # スイッチのOn/Offの状態
#    print (i,bin(i))

    # 各ライトについて
    for j in range(m):
        sum = 0
        for x in s[j]:
            sum += i >> x-1
        if sum%2==p[j]:
            c += 1
        if c == m:
            ans += 1

print (ans)
