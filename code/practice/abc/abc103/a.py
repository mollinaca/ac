#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = sorted(list(map(int,input().split())),reverse=True)
print ((l[0]-l[1])+(l[1]-l[2]))
