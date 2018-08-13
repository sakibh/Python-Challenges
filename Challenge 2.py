#!/usr/bin/env python

'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

######################################### SOLUTION #############################################

n = int(raw_input("Enter a number: "))
a = 1

for i in range(1,n+1):
        a = i * a
print a        
