#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
i = 0
while True:
    s = s[:-2]
    if s[0:(len(s)//2)] == s[(len(s)//2):len(s)]:
        print (len(s))
        exit ()