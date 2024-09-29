#!/usr/bin/python3

def perform_operation (num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    
    match operation:
        case "add":
            ans = num1 + num2
            return ans
            
        case "subtract":
            ans = num1 - num2
            return ans
            
        case "multiply":
            ans = num1 * num2
            return ans
            
        case "divide":
            if num2 == 0:
                ans = 0.0
            else:
                ans = num1 / num2
            
            return ans
            
        case _:
            print("Op should be either \" add \" or \"subtract\" or \"multiply\" or \"division\" ")
            
