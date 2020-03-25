#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print ("Bad")
        exit ()
else:
    print ("Good")