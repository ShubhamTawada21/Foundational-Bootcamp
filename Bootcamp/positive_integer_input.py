class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed."):
        self.message = message
        super().__init__(self.message)

def get_positive_int():
    while True:
        try:
            user_input = input("Please enter a valid positive integer: ")
            number = int(user_input)
            
            if number < 0:
                raise NegativeNumberError(f"Invalid input ({number}): Number must be positive!")
                
            return number
            
        except ValueError:
            print("Error: That wasn't a valid integer. Please try again.\n")
        except NegativeNumberError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    print("--- Testing Safe Input Validator ---")
    valid_num = get_positive_int()
    print(f"Success! You entered a valid positive integer: {valid_num}")                                                                             