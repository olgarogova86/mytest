# Вывести кол-во ступенек
# 04/10/2018

import sys
number_of_stairs = int(sys.argv[1])
for stair in range(1, number_of_stairs+1):
            print(" "*(number_of_stairs-stair)+"#"*stair)
