#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
count=0
while True:
    for i in range(len(l)):
        if l[i]%2 == 1:
            print (count)
            exit (0)
        l[i] = l[i]/2
    count+=1