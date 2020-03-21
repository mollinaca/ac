#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
s = input()
 
if len(s) > 9:
    print ("NO")
else:
    p = 'A?KIHA?BA?RA?'
    r = re.compile(p)
    result = r.match(s)
    if result:
        print ("YES")
    else:
        print ("NO")