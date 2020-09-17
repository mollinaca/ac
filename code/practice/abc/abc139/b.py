#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = map(int,input().split())

tap = 1
ans = 0
while True:
    if tap >= b:
        print (ans)
        exit ()
    else:
        tap += a-1
        ans += 1
