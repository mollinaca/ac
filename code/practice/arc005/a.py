#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(input().split())
ans = 0
for w in l:
    w = w.replace('.','')
    if w == 'TAKAHASHIKUN':
        ans += 1
    elif w == 'Takahashikun':
        ans += 1
    elif w == 'takahashikun':
        ans += 1
    else:
        pass

print (ans)
