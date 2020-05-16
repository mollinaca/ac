#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())
print (c) if a*c <= b else print (b//a)
