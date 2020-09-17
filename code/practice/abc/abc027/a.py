#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(int,input().split()))
for i in l:
    if l.count(i) == 1 or l.count(i) == 3:
        print (i)
        exit ()
