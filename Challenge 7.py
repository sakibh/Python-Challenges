#!/usr/bin/env python

#Question 7
#Level 2


raw_data = raw_input("Enter X,Y Values: ")
split_data = [int(i) for i in raw_data.split(",")]

print split_data

X = int(split_data[0])
Y = int(split_data[1])
twoD_list = [[0 for column in range(Y)] for row in range(X)]

for row in range(X):
    for col in range(Y):
        twoD_list[row][col] = row*col

print twoD_list