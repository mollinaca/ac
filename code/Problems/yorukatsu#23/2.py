#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = int(input())
a = 1

for i in range(1, x):
  for j in range(2, x):
    if i**j > x:
      break
    a = max(a, i**j)

print(a)
