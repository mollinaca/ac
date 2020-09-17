#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
M = 0
A = 0
R = 0
C = 0
H = 0
for _ in range(n):
    x = input()[0]
    if x == "M":
        M += 1
    elif x == "A":
        A += 1
    elif x == "R":
        R += 1
    elif x == "C":
        C += 1
    elif x == "H":
        H += 1
    else:
        pass
print ((M*A*R)+(M*A*C)+(M*A*H)+(M*R*C)+(M*R*H)+(M*C*H)+(A*R*C)+(A*R*H)+(A*C*H)+(R*C*H))
