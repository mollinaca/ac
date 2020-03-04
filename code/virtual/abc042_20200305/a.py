#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(int, input().split()))
if min(l) == 5:
    l.remove(5)
    if min(l) == 5:
        l.remove(5)
        if min(l) == 7:
            print ("YES")
            exit ()
print ("NO")