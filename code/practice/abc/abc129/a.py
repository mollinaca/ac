#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(int, input().split()))
total = 0
for _ in range(2):
    total += min(l)
    l.remove(min(l))
print (total)