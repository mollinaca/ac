#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = map(str,input().split())

if a == "H":
    if b == "H":
        print ("H")
    else:
        print ("D")
else:
    if b == "H":
        print ("D")
    else:
        print ("H")
