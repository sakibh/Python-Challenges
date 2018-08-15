#!/usr/bin/env python

'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class String(object):
        def _init_(self, data):
            self.data = data

        def getString(self):
            self.data = raw_input("Enter string: ")

        def printString(self):
            string = self.data
            print string.upper()

start = String()
start.getString()
start.printString()