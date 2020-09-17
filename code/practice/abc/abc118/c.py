#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))

import fractions
from functools import reduce

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

print (gcd_list(A))
