#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
menu = []
for _ in range(n):
    menu.append(int(input()))
print (sorted(set(menu),reverse=True)[1])
