#!/usr/bin/env python3

size = int(input("Enter the size of the pattern: "))

iteration = 0

while(iteration < size):
    for number in range(0, size):
        print("*", end="")

    print("\n")
    iteration += 1 # == iteration = iteration + 1 -= *=
    
    
