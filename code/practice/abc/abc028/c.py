#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
l = list(map(int,input().split()))
a = []
for v in itertools.combinations(l, 3):
    a.append(sum(v))

print (sorted(a)[-3])
