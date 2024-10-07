def unit_converter():
    print("Unit Converter Calculator")
    print("Available conversions:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")

    choice = input("Enter your choice (1-4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please run the program again.")
        return

    value = float(input("Enter the value to convert: "))

    if choice == '1':
        result = value * 3.28084
        print(f"{value} meters is equal to {result:.2f} feet")
    elif choice == '2':
        result = value / 3.28084
        print(f"{value} feet is equal to {result:.2f} meters")
    elif choice == '3':
        result = value * 0.621371
        print(f"{value} kilometers is equal to {result:.2f} miles")
    elif choice == '4':
        result = value / 0.621371
        print(f"{value} miles is equal to {result:.2f} kilometers")

if __name__ == "__main__":
    unit_converter()
