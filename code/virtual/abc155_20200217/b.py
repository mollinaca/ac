#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int, input().split()))
for value in l:
    if value%2 == 0:
        if value%3 != 0 and value%5 != 0:
            print ("DENIED")
            exit (0)
print ("APPROVED")