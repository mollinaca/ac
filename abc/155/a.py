#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a, b, c = map(int, input().split())
if a == b and a != c:
    print ("Yes")
elif a == c and a != b:
    print ("Yes")
elif b == c and b != a:
    print ("Yes")
else:
    print ("No")
