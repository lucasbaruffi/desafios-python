# Given the string representations of two integers, return the string representation of the sum of those integers.
# 
# For example:
# 
# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
# 
# I have removed the use of BigInteger and BigDecimal in java
# 
# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

from sys import set_int_max_str_digits
set_int_max_str_digits(0)

def sum_strings(x=0, y=0):
    if not x:
        x = "0"
    if not y:
        y = "0"
    return str((int(x)) + (int(y)))

print(sum_strings("0", ""))

# É isso, mas o Kata impôs limitação de 12000ms, então não foi possível