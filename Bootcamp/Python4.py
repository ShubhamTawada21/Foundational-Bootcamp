def detect_type(value_str):
    try:
        int(value_str)
        return int, int(value_str)
    except ValueError:
        pass
    try:      
        float(value_str)
        return float, float(value_str)
    except ValueError:
        pass
    return str, value_str

user_input = input("Enter a value: ")
detected, converted_value = detect_type(user_input)
print(f"type: {detected.__name__}")
print(f"Value: {converted_value}")
print(f"isinstance: {isinstance(converted_value, detected)}")

