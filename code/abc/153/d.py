#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h = int(input())
for i in range(41):
    if h < 2**i:
        print ((2**i)-1)
        exit (0)