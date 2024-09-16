def convert_celsius_to_fahrenheit():
    try:
        celsius = int(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit}")
        
        ratio = fahrenheit / celsius
        print(f"Fahrenheit to Celsius ratio: {ratio}")
        
    except ValueError:
        print("Invalid input")
        
    except ZeroDivisionError:
        print("Celsius cannot be zero")

convert_celsius_to_fahrenheit()
