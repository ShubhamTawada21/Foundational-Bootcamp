def calculate_salary(basic_salary):
    hra = 0.20 * basic_salary
    da = 0.15 * basic_salary

    gross_salary = basic_salary + hra + da

    tax = 0.10 * gross_salary

    net_salary = gross_salary - tax
    
    return gross_salary, net_salary

employee_list = []

print("--- Employee Salary Calculation System ---")


while True:
    print("\nEnter Employee Details:")
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    
    gross, net = calculate_salary(basic)

    employee_data = {
        "id": emp_id,
        "name": name,
        "gross": gross,
        "net": net
    }
    employee_list.append(employee_data)

    choice = input("\nDo you want to add another employee? (yes/no): ").strip().lower()
    if choice != 'yes':
        break

# --- Display Results ---
print("\n================ Salary Summary ================")
for emp in employee_list:
    print(f"\nEmployee ID: {emp['id']}")
    print(f"Name       : {emp['name']}")
    print(f"Gross Salary: {emp['gross']:.2f}")
    print(f"Net Salary  : {emp['net']:.2f}")
    print("-" * 30)

print("\nThank you for using the system!")