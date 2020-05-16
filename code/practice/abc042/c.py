#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
D = list(map(int,input().split()))

ans = n
while True:
    for i in list(map(int, str(ans))):
        if i in D:
            break
    else:
        print (ans)
        exit ()

    ans += 1
