#!/usr/bin/env python
num1 = int(input("Enter a number to see its multiplication table: "))

for i in range (1, 11):
    answer = num1 * i
    print("{0} * {1} = {2}".format(num1, i, answer))
    
