#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = sorted(input(),reverse=False)
t = sorted(input(),reverse=True)
print ("Yes") if s < t else print ("No")
