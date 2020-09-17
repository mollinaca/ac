#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
ans = 0

while True:
    p_len_s = len(s)
    for i in range(len(s)):
        if i == 0:
            pass
        else:
            if (s[i] == '0' and s[i-1] == '1') or (s[i] == '1' and s[i-1] == '0'):
                s = s[0:i-1] + s[i+1::]
                ans += 2

                if len(s) < 2:
                    print (ans)
                    exit ()

                if s == '10' or s == '01':
                    print (ans+2)
                    exit ()

                break

    a_len_s = len(s)
    if p_len_s == a_len_s:
        print (ans)
        exit ()
