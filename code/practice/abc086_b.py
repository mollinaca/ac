#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

str = list(map(str, input().split()))
ab = int(str[0] + str[1])

if math.sqrt(ab).is_integer():
    print ("Yes")
    exit (0)

print("No")
