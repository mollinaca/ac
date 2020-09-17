#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
print (0) if a%b == 0 else print ((b*((a//b)+1))-a)
