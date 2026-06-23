class InvalidMarksError(Exception):
    pass

def get_student_marks():
    while True:
        try:
            marks = float(input("Enter Student Marks (0-100): "))
            
            if marks < 0 or marks > 100:
                raise InvalidMarksError("Marks must be between 0 and 100!")
            
            return marks
            
        except ValueError:
            print("❌ Invalid Input! Please enter a valid number (e.g., 85 or 92.5).\n")
            
        except InvalidMarksError as error:
            print(f"❌ Logical Error: {error}\n")

def calculate_class_average(total_marks, total_students):
    try:
        average = total_marks / total_students
        return average
    except ZeroDivisionError:
        return 0.0

print("--- Safe Marks Analyzer ---")
valid_marks = get_student_marks()
print(f"Successfully recorded marks: {valid_marks}")