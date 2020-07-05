#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
print (0) if int(s[-3::]) == 0 else print (1000-int(s[-3::]))
