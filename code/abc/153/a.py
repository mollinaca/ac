#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,a = map(int, input().split())
if (h%a) == 0:
    print (h//a)
else:
    print ((h//a)+1)
