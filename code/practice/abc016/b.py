#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())
if a+b == c:
    plus = True
else:
    plus = False

if a-b == c:
    minus = True
else:
    minus = False

if plus and minus:
    print ("?")
elif plus and not minus:
    print ("+")
elif not plus and minus:
    print ("-")
else: # not plus and not minus
    print ("!")
