#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
c = 0
ans = ''

for i in range(len(s)):
    if i == 0:
        p = s[0]
        c = 1
    elif i == len(s)-1:
        if s[i] == p:
            c += 1
            ans += p + str(c)
        else:
            ans += p + str(c)
            ans += s[i] + str(1)
    else:
        if s[i] == p:
            c += 1
        else:
            ans += p + str(c)
            p = s[i]
            c = 1
print (ans)
