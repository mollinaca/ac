#!/usr/bin/env python3
# -*- coding: utf-8 -*-
m,n,N = map(int,input().split())

ans = 0
amari = 0
empitsu = N
while True:
    ans += empitsu
    kaisyu = empitsu
    kaisyu += amari

    if kaisyu < m:
        break

    empitsu = (kaisyu//m)*n
    amari = kaisyu%m

print (ans)
