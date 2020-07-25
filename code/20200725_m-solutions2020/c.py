#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
A = list(map(int,input().split()))
for i in range(k,n):
    print ("Yes") if A[i-k] < A[i] else print ("No")
