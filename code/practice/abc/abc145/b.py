#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
s = input()
if n%2 == 1:
    print ("No")
else:
    if s[0:(n//2)] == s[n//2::]:
        print ("Yes")
    else:
        print ("No")
