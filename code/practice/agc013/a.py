#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))

state = None # inc,dec,same
c = 0

for i in range(1,len(A)):
    if A[i] > A[i-1]:
        if state == None:
            state = "inc"
        elif state == "inc":
            pass
        elif state == "dec":
            c += 1
            state = None
        elif state == "same":
            state = "inc"
        else:
            pass

    elif A[i] < A[i-1]:
        if state == None:
            state = "dec"
        elif state == "dec":
            pass
        elif state == "inc":
            c += 1
            state = None
        elif state == "same":
            state = "dec"
        else:
            pass
    else:
        state = "same"

print (c+1)
