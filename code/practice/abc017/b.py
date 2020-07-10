#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
s = s.replace('ch','').replace('o','').replace('k','').replace('u','')
print ("YES") if len(s) == 0 else print ("NO")
