#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
print (((1900*m)+100*(n-m))*(2**m))
