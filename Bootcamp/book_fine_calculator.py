total_fine_collected = 0
highest_fine = 0
total_students = 0

print("--- Library Fine Calculator ---")

while True:
    student_name = input("\nEnter student name (or type 'exit' to finish): ")
    
    if student_name.lower() == 'exit':
        break
        
    days_late = int(input("Enter days late: "))
    
    individual_fine = 0
    
    if 1 <= days_late <= 5:
        individual_fine = days_late * 5
    elif 6 <= days_late <= 10:
        individual_fine = days_late * 10
    elif days_late > 10:
        individual_fine = days_late * 20
    else:
        individual_fine = 0 
    
    print(f"Individual Fine for {student_name}: ₹{individual_fine}")
    
    total_fine_collected = total_fine_collected + individual_fine
    total_students = total_students + 1
    
    if individual_fine > highest_fine:
        highest_fine = individual_fine

print("\n---------------------------------")
print("         FINAL SUMMARY           ")
print("---------------------------------")
print(f"Total Fine Collected: ₹{total_fine_collected}")
print(f"Highest Fine:         ₹{highest_fine}")

if total_students > 0:
    average_fine = total_fine_collected / total_students
    print(f"Average Fine:         ₹{average_fine:.2f}")