#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
p = list(map(int,input().split()))
ex = [1/2*(i+1) for i in p]
total = [0]

for i in range(N):
    total.append (total[i] + ex[i])

ans = 0
for i in range(N+1-K):
    tmp = total[i+K] - total[i]
    if ans < tmp:
        ans = tmp

print (ans)
