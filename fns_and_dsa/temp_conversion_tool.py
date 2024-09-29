#!/usr/bin/python3
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    ans = ( fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return ans 
    
def convert_to_fahrenheit(celsius):
   ans = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
   return ans 
