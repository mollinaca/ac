#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from decimal import Decimal
a,b = map(Decimal, input().split())
print (math.floor(a*b))
