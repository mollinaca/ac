#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
m = n%k
print (min(abs(k-m),m))
