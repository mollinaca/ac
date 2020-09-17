#!/usr/bin/env python3
# -*- coding: utf-8 -*-
grid = []
for _ in range(4):
    grid.append(list(map(str, input().split())))

for line in reversed(grid):
    print(' '.join(map(str, reversed(line))))
