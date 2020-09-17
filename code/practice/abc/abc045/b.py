#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sa = list(input())
sb = list(input())
sc = list(input())
n = "a"
while True:
    if n == "a":
        if len(sa) == 0:
            print ("A")
            exit ()
        n = sa.pop(0)
    elif n == "b":
        if len(sb) == 0:
            print ("B")
            exit ()
        n = sb.pop(0)
    else:
        if len(sc) == 0:
            print ("C")
            exit ()
        n = sc.pop(0) 