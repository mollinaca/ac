#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
s = input()
for i in range(len(s)):
    print (chr(ord(s[i])+n), end="") if ord(s[i])+n <= 90 else print (chr(ord(s[i])+n-26), end="")
print ()
