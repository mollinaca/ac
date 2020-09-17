#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())
print ("Yes") if (a+b == c) or (a+c == b) or (b+c == a) else print ("No")