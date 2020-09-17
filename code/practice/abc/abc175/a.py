#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
if s == 'RRR':
    print (3)
elif s.count('RR') == 1:
    print (2)
elif s.count('R') == 1 or s.count('R') == 2:
    print (1)
else:
    print (0)
