#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = 1
x = 0
while True:
    if a[x] == 2:
        print (ans)
        exit ()

    if ans > len(a):
        print (-1)
        exit ()

    x = a[x]-1
    ans += 1
