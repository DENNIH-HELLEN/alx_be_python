#!/usr/bin/python

m1 = int(input("Enter your monthly income: "))

m2 = int(input("Enter your monthly expenses: "))

m3 = m1 - m2

ps = (m3 * 12 + (m3 * 12 * 0.05))

print("Your monthly savings are ${0:d}.".format(m3))

print("Projected savings after one year, with interest, is: ${0:.0f}.".format(ps))

