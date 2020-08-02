#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k = int(input())

"""
7の数をインクリメントしながら毎回 mod を求める
 → 無限に求める必要があり終われない...
"""

if k%2 == 0 or k%5 == 0:
    print (-1)
    exit ()

x = 7
while True:
    print (str(x).count('7'))
    if x%k == 0:
        print (str(x).count('7'))
        exit ()

#    if x > k:
#        print (-1)
#        exit ()

    x = int(str(x)+'7')