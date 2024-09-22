#!/usr/bin/python3

inpt= input("What's the weather like today? (sunny/rainy/cold): ")

if inpt == "sunny":
    print("Wear a t-shirt and sunglasses.")
 
elif inpt == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif inpt == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")

