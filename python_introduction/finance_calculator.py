#!/usr/bin/python

m1 = int(input("Enter your monthly income: "))

m2 = int(input("Enter your monthly expenses: "))

m3 = m1 - m2

interest = m3 * 12 * 0.05

ps = m3 * 12 + interest

print("Your monthly savings are ${0:d}.".format(m3))

print("Projected savings after one year, with interest, is: ${0:.0f}.".format(ps))

