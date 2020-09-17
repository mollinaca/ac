#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
n = int(input())
for line in itertools.product("abc",repeat=n):
    print(''.join(line))
