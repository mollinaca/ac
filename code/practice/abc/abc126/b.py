#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
if (1 <= int(s[0:2]) and int(s[0:2]) <= 12) and (1 <= int(s[2:4]) and int(s[2:4]) <= 12):
    ans = "AMBIGUOUS"
elif (1 <= int(s[0:2]) and int(s[0:2]) <= 12) and (1 > int(s[2:4]) or int(s[2:4]) > 12):
    ans = "MMYY"
elif (1 > int(s[0:2]) or int(s[0:2]) > 12) and (1 <= int(s[2:4]) and int(s[2:4]) <= 12):
    ans = "YYMM"
else:
    ans = "NA"
print (ans)
