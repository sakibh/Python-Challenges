#!/usr/bin/env python

'''
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

numbers = []

for i in range(2000,3201):
    if (i%7 == 0) and (i%5 != 0):
        numbers.append(str(i))
print ','.join(numbers)