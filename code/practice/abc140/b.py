#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

score = 0
for i in range(len(A)):
#    print (f"i={i},A[i]-1={A[i]-1},B={B[A[i]-1]}")
    score += B[A[i]-1]

    if i != len(A)-1:
        if A[i+1] == A[i] + 1:
#            print (f"c,C[A[i]-1]={C[A[i]-1]}")
            score += C[A[i]-1]
#    print (f"score={score}")
print (score)
