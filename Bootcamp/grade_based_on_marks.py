marks = int(input("Enter student's marks: "))

if marks >= 40:
    print("Pass")
    if marks >= 90:
        print("Distinction")
    elif marks >= 75:
        print("First Division")
    elif marks >= 60:
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Fail")
