#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

for x in range(1,n+1):
    ans = 0
    found = []

    for i in range(1,101):
        if i in found:
            break
        for j in range(i,101):
            if j in found:
                break
            for k in range(j,101):
                if k in found:
                    break

                if i**2 + j**2 + k**2 + i*j + j*k + k*i == x:
                    ans += 3**(len(set([i,j,k]))-1)
                    if i not in found:
                        found.append(i)
                    if j not in found:
                        found.append(j)
                    if k not in found:
                        found.append(k)
                    break
                elif x < i**2 + j**2 + k**2 + i*j + j*k + k*i:
                    break
                else:
                    pass
    print (ans)
