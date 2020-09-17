#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,x = map(int,input().split())

ans = 0
over = (10**9)+1

while over - ans > 1:
    avg = int((ans+over)/2)
    if a*avg+b*len(str(avg)) <= x:
        ans = avg
    else:
        over = avg

print (ans)
