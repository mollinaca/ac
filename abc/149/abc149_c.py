#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())

def pr(n):
    for p in range(2, n):
        if n % p == 0:
            return False
    return True

while True:
    if pr(n):
        break
    n+=1

print (n)