#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
x = ((n+1)*n)//2

def isPrime (x:int) -> bool:
    if x == 1:
        return False

    d = int(x**(1/2)) + 1
    for i in range(2,d):
        if x % i == 0:
            return False
    return True

print ('WANWAN') if isPrime(x) else print ('BOWWOW')
