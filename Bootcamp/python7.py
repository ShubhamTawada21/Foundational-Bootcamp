print("===unit converter===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kilometers to Meters")
print("4. Meters to Kilometers")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")

elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")

elif choice == '3':
    kilometers = float(input("Enter distance in Kilometers: "))
    meters = kilometers * 1000
    print(f"{kilometers} km is equal to {meters} m")

elif choice == '4':
    meters = float(input("Enter distance in Meters: "))
    kilometers = meters / 1000
    print(f"{meters} m is equal to {kilometers} km")

else:
    print("Invalid choice! Please select a valid option (1-4).")

    