#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
c = 0
ans = []
while n > 0:
    if 8 <= n:
        ans.append(8)
        n = n-8
        c += 1
    elif 4 <= n < 8:
        ans.append(4)
        n = n-4
        c += 1
    elif 2 <= n < 4:
        ans.append(2)
        n = n-2
        c += 1
    else: # n == 1
        ans.append(1)
        n = n-1
        c += 1

print (c)
for i in ans:
    print (i)
