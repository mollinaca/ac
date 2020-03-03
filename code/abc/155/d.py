#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n, k = map(int, input().split())
a = list(map(int, input().split()))

# 全探索
seki_list = []
for i in range(n):
    for j in range(n):
        if i == j:
            pass
        elif j < i:
            pass
        else:
            seki_list.append(a[i]*a[j])

print (sorted(seki_list)[k-1])