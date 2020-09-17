#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
txa,tya,txb,tyb,t,v = map(int,input().split())
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    a = math.sqrt(((x-txa)**2)+((y-tya)**2))
    b = math.sqrt(((txb-x)**2)+((tyb-y)**2))
    if a+b <= t*v:
        print ("YES")
        exit ()
print ("NO")
