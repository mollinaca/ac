#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
d,x = map(int,input().split())
ans = 0
for _ in range(n):
    a = int(input())
    ans += (-(-d//a))
print (ans+x)
