#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
s = []
for _ in range(n):
    s.append(input())

ans = ""
for i in range(n//2):
#    print (i,-(i+1),s[i],s[-(i+1)])
    if set(s[i]) & set(s[-(i+1)]):
        x = set(s[i]) & set(s[-(i+1)])
        ans += list(x)[0]
    else:
        print (-1)
        exit ()

if n%2 == 0:
    print (ans+ans[::-1])
else:
    y = s[n//2][0]
    print (ans+y+ans[::-1])
