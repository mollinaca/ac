#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
print ("Yes") if n%(sum(list(map(int, str(n))))) == 0 else print ("No")
