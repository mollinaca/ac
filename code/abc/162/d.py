#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
S = input()

c = 0
for i in range(N-2):
    for j in range(i,N-1):
        for k in range(j,N):
            if j-i == k-j:
                pass
            else:
                if S[i] != S[j]:
                    if S[j] != S[k]:
                        if S[k] != S[i]:
                            c += 1
print (c)
