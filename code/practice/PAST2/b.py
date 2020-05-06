#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
s = input()
c = Counter(s)
print (max(c, key=c.get))
