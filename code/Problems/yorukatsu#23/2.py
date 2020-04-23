#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = int(input())

def prime_factorize (n:int):
    l = []
    if n == 1:
        l.append(1)
        return l

    while n % 2 == 0:
        l.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            l.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        l.append(n)
    return l

def judge (p:int):
    if p == 1:
        return True

    l = prime_factorize(p)
    print (p,l)
    if len(set(l)) == 1 and len(l) > 1:
        return True
    else:
        return False

for i in range(x,0,-1):
    if judge(i):
        print (i)
        exit ()
