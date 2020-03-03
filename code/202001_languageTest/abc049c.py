#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
s = input()

if re.fullmatch(r"(dream|dreamer|erase|eraser)+", s):
    print("YES")
else:
    print("NO")