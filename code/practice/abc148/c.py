#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fractions
a,b = map(int,input().split())
print (a // fractions.gcd(a, b) * b)
