#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
shiritori = []
for _ in range(n):
    shiritori.append(input())

if len(set(shiritori)) != n:
    print ("No")
    exit ()

for i in range(n-1):
    if shiritori[i][-1] != shiritori[i+1][0]:
        print ("No")
        exit ()
else:
    print ("Yes")
