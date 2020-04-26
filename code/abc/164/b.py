#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c,d = map(int,input().split())
print ("Yes") if -(-a//d) >= -(-c//b) else print ("No")
