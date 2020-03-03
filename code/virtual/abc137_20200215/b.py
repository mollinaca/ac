#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k, x = map(int, input().split())
ans=[]
for i in range(x-(k-1), x+(k-1)+1):
    ans.append(i)
print(' '.join(map(str, ans)))
