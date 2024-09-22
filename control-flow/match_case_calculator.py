#!/usr/bin/python3
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        num3 = num1+num2
        print("The result is %d' ", int(num3))

    case "-":
        print("The result is " ,int(num1 - num2))
    case "*":
        print("The result is " ,int(num1 * num2))
    case "/":
        print("The result is ",int(num1 / num2))




