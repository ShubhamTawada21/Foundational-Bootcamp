temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("Wear a heavy coat")

elif 0 <= temperature <= 15:
    print("Wear a jacket")

elif 16 <= temperature <= 30:
    print("Comfortable weather")

else:
    print("Wear light clothing and stay hydrated")

