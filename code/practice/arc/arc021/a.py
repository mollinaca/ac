#!/usr/bin/env python3
# -*- coding: utf-8 -*-
grid = [list(input().split()) for i in range(4)]

for i in range(4):
    for j in range(4):
        if i == 0 and j == 0:
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]:
                print ("CONTINUE")
                exit ()
        elif i == 0 and j == 3:
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j-1]:
                print ("CONTINUE")
                exit ()
        elif i == 3 and j == 0:
            if grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i][j+1]:
                print ("CONTINUE")
                exit ()
        elif i == 3 and j == 3:
            if grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i][j-1]:
                print ("CONTINUE")
                exit ()
        elif i == 0 and (j != 0 or j != 3):
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i][j+1]:
                print ("CONTINUE")
                exit ()
        elif i == 3 and (j != 0 or j != 3):
            if grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i][j+1]:
                print ("CONTINUE")
                exit ()
        elif (i != 0 or i != 3) and j == 0:
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i][j+1]:
                print ("CONTINUE")
                exit ()
        elif (i != 0 or i != 3) and j == 3:
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i][j-1]:
                print ("CONTINUE")
                exit ()
        else:
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i][j-1]:
                print ("CONTINUE")
                exit ()

print ("GAMEOVER")
