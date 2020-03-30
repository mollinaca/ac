#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
A.append(0)
A.insert(0,0)
A_sort = sorted(A)
S = (abs(A_sort[0] - A_sort[-1]))*2
for i in range(len(A)):
    if i == 0 or i == len(A)-1:
        pass
    else:
        print (S + abs(A[i-1]-A[i+1]) - (abs(A[i-1]-A[i]) + abs(A[i]-A[i+1])))
