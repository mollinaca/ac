#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
s = input()
for i in range(len(s)):
    if i == k-1:
        print (s[i].lower(),end="")
    else:
        print (s[i],end="")
print ()
