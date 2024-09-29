CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9



def convert_to_celsius(fahrenheit):
    ans = ( fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return ans 
    
def convert_to_fahrenheit(celsius):
   ans = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
   return ans 


def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    func = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    match func:
        case "C":
            ans = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {ans}°F")
        case "F":
            ans = convert_to_celsius(temp)
            print(f"{temp}°F is {ans}°C")
        case _:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
