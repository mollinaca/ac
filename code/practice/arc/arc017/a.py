#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

def isPrime (x:int) -> bool:
    d = int(x**(1/2)) + 1

    for i in range(2,d):
        if x % i == 0:
            return False
    return True

print ("YES") if isPrime(n) else print ("NO")
