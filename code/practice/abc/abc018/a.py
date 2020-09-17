#!/usr/bin/env python3
# -*- coding: utf-8 -*-
taro = int(input())
jiro = int(input())
saburo = int(input())

if jiro < taro and saburo < taro: # taro 1
    print (1)
    if saburo < jiro:
        print (2)
        print (3)
    else:
        print (3)
        print (2)
elif (taro < jiro and saburo < taro) or (jiro < taro and taro < saburo): # taro 2
    print (2)
    if saburo < jiro:
        print (1)
        print (3)
    else:
        print (3)
        print (1)
else: #taro 3
    print (3)
    if saburo < jiro:
        print (1)
        print (2)
    else:
        print (2)
        print (1)
