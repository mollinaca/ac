#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,x = map(int,input().split())
a = sorted(list(map(int,input().split())))

ans = 0
for i in range(len(a)):
    if not i == len(a)-1:
        if x > a[i]:
            ans += 1
            x = x-a[i]
        elif x == a[i]:
            ans += 1
            break
        else: #x < a[i]
            break
    else:
        if x == a[i]:
            ans += 1
        else:
            pass

print (ans)
