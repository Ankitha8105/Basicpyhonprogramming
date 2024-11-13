'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 09-11-2024
    @Title : Temperature Converstion problem
'''
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius.

    Returns:
        Temperature in Fahrenheit.
    """

    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in Fahrenheit.

    Returns:
        Temperature in Celsius.
    """

    return (fahrenheit - 32) * 5/9


temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

if unit.upper() == 'C':
    converted_temp = celsius_to_fahrenheit(temperature) 

    print(f"{temperature}°C is {converted_temp}°F")
elif unit.upper() == 'F':
    converted_temp = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
else:
    print("Invalid unit.")