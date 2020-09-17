#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
total = sum(list(map(int, str(n))))
print ("Yes") if n%total == 0 else print ("No")
