#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

i = 0

if n == ng1 or n == ng2 or n == ng3:
    print ("NO")
    exit ()

while n > 0:
    n -= 3
    if n == ng1 or n == ng2 or n == ng3:
        n += 1
        if n == ng1 or n == ng2 or n == ng3:
            n += 1
            if n == ng1 or n == ng2 or n == ng3:
                print ("NO")
                exit ()
    i += 1
    if 100 < i:
        print ("NO")
        exit ()
print ("YES")
