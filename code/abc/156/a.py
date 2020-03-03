#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,r = map(int, input().split())
print (100*(10-n)+r) if n < 10 else print (r)