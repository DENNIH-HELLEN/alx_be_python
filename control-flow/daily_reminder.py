#!/usr/bin/env python

task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

timeBound = input("Is it time-bound? (yes/no): ")


match priority:

    case "high":
        if timeBound == "yes":
            print("Reminder: '{0}' is a {1} priority task that requires immediate attention today!".format(task, priority))
        elif timeBound == "no":
            print("Note: '{0}' is a {1} priority task. Consider completing it when you have free time.".format(task, priority))
        else:
            print("Error: Answer \"yes\" or \"no \" ")

    case "medium":
        if timeBound == "yes":
            print("Reminder: '{0}' is a {1} priority task that requires immediate attention today!".format(task, priority))
        elif timeBound == "no":
            print("Note: '{0}' is a {1} priority task. Consider completing it when you have free time.".format(task, priority))
        else:
            print("Error: Answer \"yes\" or \"no \" ")

    case "low":
        if timeBound == "yes":
            print("Reminder: '{0}' is a {1} priority task that requires immediate attention today!".format(task, priority))
        elif timeBound == "no":
            print("Note: '{0}' is a {1} priority task. Consider completing it when you have free time.".format(task, priority))
        else:
            print("Error: Answer \"yes\" or \"no \" ")

    case _:
        print("Error: Please answer using \"high\" or \"low\" or \"medium\" ")
        
