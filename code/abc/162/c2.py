#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k = int(input())

import math
#from functools import reduce
#def gcd(*numbers):
#    return reduce(math.gcd, numbers)

total = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        tmp = math.gcd(a,b)
        for c in range(1,k+1):
            total += math.gcd(tmp,c)
print (total)
