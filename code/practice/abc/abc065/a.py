#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,a,b = map(int,input().split())
if b <= a:
    print ("delicious")
else:
    if b-a <= x:
        print ("safe")
    else:
        print ("dangerous")
