#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
t = input()
for i in range(len(s)):
    if s[i] == t[i]:
        pass
    elif s[i] == "@":
        if not t[i] in "atcoder@":
            print ("You will lose")
            exit ()
    elif t[i] == "@":
        if not s[i] in "atcoder@":
            print ("You will lose")
            exit ()
    else:
        print ("You will lose")
        exit ()
print ("You can win")