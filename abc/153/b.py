#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h, n = map(int, input().split())
n_list = [int(i) for i in input().split()] 
n_list.sort()

for dmg in n_list:
    h = h - dmg
    if h <= 0:
        print ("Yes")
        exit (0)

print ("No")
