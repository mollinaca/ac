#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()[::-1]
while True:
    if len(s) == 0:
        print ("YES")
        exit ()

    if s[0:5] == "maerd" or s[0:5] == "esare":
        s = s[5:]
    else:
        if s[0:6] == "resare":
            s = s[6:]
        else:
            if s[0:7] == "remaerd":
                s = s[7:]
            else:
                print ("NO")
                exit ()
