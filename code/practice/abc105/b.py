#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
count = 0

def divs(n:int):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    # divs.sort()
    return divs

for i in range(1,n+1,2):
    if len(divs(i)) == 8:
        count += 1
print (count)