# Сумма цифр в строке
# 01/10/2018

import sys
digit_string = sys.argv[1]
sum_of_digit = sum(map(int, list(digit_string)))
print(sum_of_digit)
