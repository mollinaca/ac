#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.py を一般化

# n = 入力される商品数
# m = 所持金
n,m = map(int,input().split())

# a1,p1 = 商品名、値段
# ...
# an,pn

item = []
for _ in range(n):
    l = list(map(int,input().split()))
    item.append(l)

#print (item)
for i in range(2**n):
    bag = []
    price = 0
    for j in range(n):
        if ((i>>j)&1):
            bag.append(item[j][0])
            price += item[j][1]

    if price <= m:
        print (price,bag)
