#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
print ('16:9') if n%16 == 0 and m%9 == 0 else print ('4:3')
