#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
k = int(input())

for i in range(k):
    if s[i] != '1':
        print (s[i])
        exit ()
else:
    print ('1')
