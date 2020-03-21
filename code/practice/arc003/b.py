#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = []
for _ in range(n):
    l.append(input()[::-1])
for v in sorted(l):
    print (v[::-1])
