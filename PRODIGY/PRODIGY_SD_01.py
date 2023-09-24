def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def main():
    print("Temperature Conversion Program")
    print("Available units: Celsius, Fahrenheit, Kelvin")

    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit (Celsius, Fahrenheit, Kelvin): ").lower()

    if original_unit == "celsius":
        converted_fahrenheit = celsius_to_fahrenheit(temperature)
        converted_kelvin = celsius_to_kelvin(temperature)
    elif original_unit == "fahrenheit":
        converted_celsius = fahrenheit_to_celsius(temperature)
        converted_kelvin = fahrenheit_to_kelvin(temperature)
    elif original_unit == "kelvin":
        converted_celsius = kelvin_to_celsius(temperature)
        converted_fahrenheit = kelvin_to_fahrenheit(temperature)
    else:
        print("Invalid input for original unit.")
        return

    print("Converted temperatures:")
    if original_unit == "celsius":
        print(f"{temperature} Celsius = {converted_fahrenheit} Fahrenheit")
        print(f"{temperature} Celsius = {converted_kelvin} Kelvin")
    elif original_unit == "fahrenheit":
        print(f"{temperature} Fahrenheit = {converted_celsius} Celsius")
        print(f"{temperature} Fahrenheit = {converted_kelvin} Kelvin")
    elif original_unit == "kelvin":
        print(f"{temperature} Kelvin = {converted_celsius} Celsius")
        print(f"{temperature} Kelvin = {converted_fahrenheit} Fahrenheit")

if __name__ == "__main__":
    main()
