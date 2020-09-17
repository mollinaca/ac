#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
ac = 0
wa = 0
wa_d = {}
ac_d = {}
for i in range(1,n+1):
    ac_d[str(i)] = False
    wa_d[str(i)] = 0

for _ in range(m):
    p,s = input().split()
    if s == "AC":
        if ac_d[p]:
            pass
        else:
            wa += wa_d[p]
            ac += 1
            ac_d[p] = True 
    else:
        wa_d[p] += 1

print (ac,wa)
