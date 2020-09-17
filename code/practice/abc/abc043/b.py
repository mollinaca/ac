#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
e = ""
for i in range(len(s)):
    if s[i] == "0" or s[i] == "1":
        e += s[i]
    else:
        if len(e) != 0:
            e = e[0:len(e)-1]
print (e)