age = int(input("Enter your age: "))
degree = input("Enter your degree (e.g., 'B.tech' , 'BCA'): ")
cgpa = float(input("Enter your CGPA: "))

if 21<= age <= 45:
    if degree in ['B.tech', 'BCA']:
        if cgpa >= 7.0:
            print("You are eligible for the job.")
        else:
            print("You are not eligible for the job due to low CGPA.")
    else:
        print("You are not eligible for the job due to degree requirements.")
else:
    print("You are not eligible for the job due to age restrictions.")