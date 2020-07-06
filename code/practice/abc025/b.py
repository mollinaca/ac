#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,a,b = map(int,input().split())
ans = 0

for _ in range(n):
    s,d = input().split()
    d = int(d)

    if s == "West":
        x = -1
    else: # East
        x = 1

    if d < a:
        ans += a*x
    elif a <= d <= b:
        ans += d*x
    else: # b < d
        ans += b*x

if ans < 0:
    print ("West",ans*-1)
elif ans > 0:
    print ("East",ans)
else: # ans == 0
    print (0)
