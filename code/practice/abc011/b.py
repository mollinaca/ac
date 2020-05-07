#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
if len(s) == 1:
    print (s.upper())
else:
    for i in range(len(s)):
        if i == 0:
            print (s[i].upper(), end="")
        else:
            print (s[i].lower(), end="")
        print
