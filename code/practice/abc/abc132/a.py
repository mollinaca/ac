#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
print ("Yes") if len(s) == 4 and len(set(s)) == 2 else print ("No")
