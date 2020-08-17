#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = []

for _ in range(n):
    x,y = map(int,input().split())
    l.append((x,y))

ans = 0
for i in range(n-1):
    for j in range(1,n):
        if i == j:
            pass
        else:
            tmp = (((l[i][0]-l[j][0])**2 + (l[i][1]-l[j][1])**2)**(1/2))
            if ans < tmp:
                ans = tmp

print (ans)
