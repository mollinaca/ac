#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
l = [s.count("a"), s.count("b"), s.count("c")]
print ("NO") if max(l) - min(l) >= 2 else print ("YES")
