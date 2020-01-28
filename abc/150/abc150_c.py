#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

n = int(input())
p_list = tuple(map(int,input().split()))	
q_list = tuple(map(int,input().split()))	

count=1
for i in itertools.permutations(range(1,n+1)):
    if i == p_list:
        num1 = count
    if i == q_list:
        num2 = count
    count += 1

if num1 - num2 <0:
    print (num2-num1)
else:
    print (num1-num2)