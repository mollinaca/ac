#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
t = input()

ans = float('inf')

for i in range(len(s)-len(t)+1):
    tmp_s = s[i:i+len(t)]
    print (tmp_s,t)
    tmp_ans = 0
    for j in range(len(t)):
        if tmp_s[j] != t[j]:
            tmp_ans += 1
    ans = min(ans, tmp_ans)

print (ans)
