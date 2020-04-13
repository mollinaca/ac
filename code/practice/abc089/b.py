#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
arare = list(input().split())
print ("Three") if len(set(arare)) == 3 else print ("Four")
