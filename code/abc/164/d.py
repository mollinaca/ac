#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = input()
c = 0
i = 0
while i < len(S):
#    print (i)
    for j in range(i+4,len(S)+1):
        s = S[i:j]
        if int(s)%2019 == 0:
#            print (i,j,s)
            c += 1
            i = j - 1
            break
    else:
        i += 1
print (c)
