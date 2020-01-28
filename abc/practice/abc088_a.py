#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
a_list=[int(i) for i in input().split()] 
count=1
alice_sum=0
bob_sum=0

while True:
    if count%2==1:
        alice_sum+=max(a_list)
    else:
        bob_sum+=max(a_list)
    a_list.remove(max(a_list))
    count+=1
    if not a_list:
        break
print (alice_sum-bob_sum)