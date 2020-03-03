#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i]%2 == 1:
        continue
    else:
        if a[i]%3 == 0:
            continue
        elif a[i]%5 == 0:
            continue
        else:
            print ("DENIED")
            exit (0)
print ("APPROVED")
