#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = list(map(int,input().split()))
p = list(map(int,input().split()))
print (max((n[0]//p[0])*(n[1]//p[1])*(n[2]//p[2]), (n[0]//p[0])*(n[1]//p[2])*(n[2]//p[1]), (n[0]//p[1])*(n[1]//p[0])*(n[2]//p[2]), (n[0]//p[1])*(n[1]//p[2])*(n[2]//p[0]), (n[0]//p[2])*(n[1]//p[1])*(n[2]//p[0]), (n[0]//p[2])*(n[1]//p[0])*(n[2]//p[1])))
