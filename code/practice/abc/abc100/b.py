#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d,n = map(int,input().split())
print ((100**d)*n) if n != 100 else print ((100**d)*101)
