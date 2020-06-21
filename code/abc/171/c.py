#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

if n%26 == 0:
    total = 0
    x = 0
    while True:
        x += 1
        if n == total+26**x:
            print ("z"*x)
            exit ()
        total += 26**x

def B(X, n):
    if (int(X/n)):
        return B(int(X/n), n)+str(X%n)+","
    return str(X%n)+","

l = list(B(n,26).split(","))
del l[-1]
print (l)
ans = ""
for i in l:
    ans += chr(96+int(i))

print (ans)
