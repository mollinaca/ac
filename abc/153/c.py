#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n, k = map(int, input().split())
h_list = [int(i) for i in input().split()]
if k >= len(h_list):
    print (0)
    exit (0)
h_list.sort(reverse=True)
del h_list[0:k]
print (sum(h_list))