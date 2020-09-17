#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
h = n//3600
m = (n-h*3600)//60
s = n-h*3600-m*60
if len(str(h)) == 1:
    h = "0"+str(h)
else:
    h = str(h)
    
if len(str(m)) == 1:
    m = "0"+str(m)
else:
    m = str(m)

if len(str(s)) == 1:
    s = "0"+str(s)
else:
    s = str(s)

print (h+":"+m+":"+s)
