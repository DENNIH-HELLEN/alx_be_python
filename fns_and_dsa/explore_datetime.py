#!/usr/bin/python3
from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    
    current_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current date and time: {current_date}")
    
    
    
    


def calculate_future_date():
    daysToBeadded = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta(days=daysToBeadded)
    
    future_date = future_date.strftime('%Y-%m-%d')
    
    print(f"Future date: {future_date}")
    
