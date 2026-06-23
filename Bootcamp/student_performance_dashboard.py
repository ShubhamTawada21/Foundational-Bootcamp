
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def main():
    print("=== STUDENT PERFORMANCE DASHBOARD INPUT ===")
    
    student_name = input("Enter Student Name: ").strip()
    roll_number = input("Enter Roll Number: ").strip()
    
    subject_marks = []
    total_marks_possible = 500
    
    for i in range(1, 6):
        while True:
            try:
                marks = float(input(f"Enter marks for Subject {i} (out of 100): "))
                if 0 <= marks <= 100:
                    subject_marks.append(marks)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numerical value.")
                
    while True:
        try:
            attendance_pct = float(input("Enter Attendance Percentage (0-100): "))
            if 0 <= attendance_pct <= 100:
                break
            print("Attendance must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
            
    while True:
        try:
            assignment_score = float(input("Enter Assignment Score (out of 100): "))
            if 0 <= assignment_score <= 100:
                break
            print("Assignment score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

    total_obtained = sum(subject_marks)
    academic_percentage = (total_obtained / total_marks_possible) * 100
    
    attendance_status = "Good" if attendance_pct >= 75 else "Low Attendance"
    
    internal_assessment_score = (academic_percentage * 0.60) + (assignment_score * 0.40)
    
    final_performance_score = (internal_assessment_score * 0.40) + (academic_percentage * 0.60)
    
    grade = calculate_grade(final_performance_score)
    
    performance_index = round(final_performance_score / 10, 2) 
    
    result_status = "PASS" if grade != "F" and attendance_pct >= 60 else "FAIL"

    scholarship_eligibility = "Eligible" if final_performance_score >= 90 and attendance_pct >= 85 else "Not Eligible"
    
    if final_performance_score >= 90:
        rank_category = "Elite / Top Tier"
    elif final_performance_score >= 75:
        rank_category = "First Class"
    elif final_performance_score >= 50:
        rank_category = "Average"
    else:
        rank_category = "Below Average"
        
    distinction_certificate = "Awarded" if academic_percentage >= 85 else "Not Awarded"

    print("\n" + "="*50)
    print(" STUDENT PERFORMANCE DASHBOARD ")
    print("="*50)
    print(f"Student Name: {student_name}")
    print(f"Roll Number: {roll_number}")
    print("-"*50)
    print("Marks Summary:")
    for idx, marks in enumerate(subject_marks, 1):
        print(f" Subject {idx}: {marks}/100")
    print("-"*50)
    print(f"Average Marks: {academic_percentage:.2f}%")
    print(f"Grade: {grade}")
    print("-"*50)
    print(f"Attendance Pct: {attendance_pct}%")
    print(f"Attendance Status: {attendance_status}")
    print("-"*50)
    print(f"Internal Assessment: {internal_assessment_score:.2f}/100")
    print(f"Final Perf. Score: {final_performance_score:.2f}/100")
    print(f"Performance Index: {performance_index} / 10.0")
    print("-"*50)
    print(f"Result Status: {result_status}")
    print("="*50)
    print(" BONUS FEATURES METRICS ")
    print("="*50)
    print(f"Scholarship Eligibility: {scholarship_eligibility}")
    print(f"Rank Category: {rank_category}")
    print(f"Distinction Certificate: {distinction_certificate}")
    print("="*50)

if __name__ == "__main__":
    main()
