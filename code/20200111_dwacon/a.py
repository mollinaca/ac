#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = {}
for i in range(0,n):
    line = input()
    l[i] = line.strip().split()
x = str(input())
time = 0

for i in range(0,n):
    if l[i][0] == x:
        l.pop(i)
        break
    l.pop(i)

for i in l:
    time += int((l[i][1]))

print (time)