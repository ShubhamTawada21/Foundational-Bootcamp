print("=== Unit Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kilometers to Miles")
print("4. Miles to Kilometers")

choice = input("Choose an option (1-4): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")

elif choice == "3":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    print(f"{kilometers} km = {miles:.2f} miles")

elif choice == "4":
    miles = float(input("Enter distance in miles: "))
    kilometers = miles * 1.60934
    print(f"{miles} miles = {kilometers:.2f} km")

else:
    print("Invalid choice. Please try again.")
