#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
list=[int(i) for i in input().split()] 

def search_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

count=0
isOdd=False
while True:
    for i in range(0,n):
        isOdd = search_odd(list[i])
        if isOdd:
            break
        list[i] = list[i]/2
    if isOdd:
        break
    count+=1
print (count)