def detect_type(value_str):
    try:
        converted_int = int(value_str)
        return int, converted_int
    except ValueError:
        pass
    
    try:
        converted_float = float(value_str)
        return float, converted_float
    except ValueError:
        pass
    
    return str, value_str


user_input = input("Enter a value: ")
detected_type, converted_value = detect_type(user_input)

print(f"Detected type: {detected_type.__name__}")
print(f"Converted value: {converted_value}")
print(f"Type check (isinstance): {isinstance(converted_value, detected_type)}")