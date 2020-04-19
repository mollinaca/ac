#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
A = list(map(int,input().split()))
print (n-sum(A)) if n >= sum(A) else print ("-1")
