#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
A = ([i for i in l if i > 0])
print (-1*(-1*sum(A)//len(A)))
