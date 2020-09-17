#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()

if len(s)%2 == 1:
    s = s[0:len(s)//2] + s[(len(s)//2)+1::]

for i in range(len(s)//2):
    if s[i] == '*' or s[-(i+1)] == '*' or s[i] == s[-(i+1)]:
        pass
    else:
        print ("NO")
        exit ()

print ("YES")
