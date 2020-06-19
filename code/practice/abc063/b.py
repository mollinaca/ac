#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
print ("yes") if len(s) == len(set(s)) else print ("no")
