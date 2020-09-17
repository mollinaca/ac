#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,k,l = map(int,input().split())
if k<l:
  print (min(a*k, b))
else:
  print (min(a*k, a*(k%l)+b*(k//l), b*(k//l+1)))
