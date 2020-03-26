#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fractions

def lcm(a:int,b:int):
    return a // fractions.gcd(a, b) * b

a,b,c,d = map(int,input().split())

# 個数
#(b-a+1)

# aからbまでの間のcの倍数の個数
x = (b//c)-(a//c)
if a%c == 0:
    x += 1

# aからbまでの間のdの倍数の個数
y = (b//d)-(a//d)
if a%d == 0:
    y += 1

# aからbまでの間のaとbの公倍数の個数
z = (b//lcm(c,d))-(a//lcm(c,d))
if a%(c*d) == 0:
    z += 1

print ((b-a+1)-((x+y)-z))