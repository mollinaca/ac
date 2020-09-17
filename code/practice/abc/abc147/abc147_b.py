#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str=input()
i=int(len(str))//2
count=0
s_count=0

while count < i:
    if str[count]  != str[(count+1)*-1]:
        s_count+=1
    count+=1
print (s_count)
