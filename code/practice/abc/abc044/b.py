#!/usr/bin/env python3
# -*- coding: utf-8 -*-
w = input()
u = set(w)
for s in u:
    if w.count(s)%2 != 0:
        print ("No")
        exit ()
else:
    print ("Yes")