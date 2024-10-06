def safe_divide (numerator, denominator):
    try:
        n = float(numerator)
        d = float(denominator)
        ans = n / d
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

    else:
        return f"The result of the division is {ans}"
