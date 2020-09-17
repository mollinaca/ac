#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(int,input()))
print ("Yes") if sum(l)%9 == 0 else print ("No")
