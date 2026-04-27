import re
import copy

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-z ]+$", name.strip()))

def is_valid_department(dept):
    return bool(re.match(r"^[A-Za-z ]+$", dept.strip()))

def is_valid_hours(hours):
    try:
        return float(hours) >= 0
    except:
        return False

def add_employee(records, name="Unknown", department="General", hours=0):
    try:
        if not is_valid_name(name):
            raise ValueError("Invalid Name")
        if not is_valid_department(department):
            raise ValueError("Invalid Department")
        if not is_valid_hours(hours):
            raise ValueError("Invalid Hours")

        name = name.strip()
        department = department.strip()
        hours = float(hours)

        # Check for duplicates
        for emp in records:
            if emp["name"].lower() == name.lower() and emp["department"].lower() == department.lower():
                print("Error: Duplicate employee found → Record not added.")
                return

        records.append({
            "name": name,
            "department": department,
            "hours": hours
        })

        print("Employee added successfully!")

    except Exception as e:
        print(f"Error: {e} → Record skipped.")

def total_hours_by_department(records):
    if not records:
        print("No data present")
        return

    dept_hours = {}
    for emp in records:
        dept = emp["department"]
        dept_hours[dept] = dept_hours.get(dept, 0) + emp["hours"]

    if not dept_hours:
        print("No data present")
        return

    print("Total Hours by Department:")
    for dept, hrs in dept_hours.items():
        print(f"{dept}: {hrs} hours")

def employees_above_hours(records, threshold):
    if not records:
        print("No data present")
        return

    found = False
    print(f"Employees working more than {threshold} hours:")

    for emp in records:
        if emp["hours"] > threshold:
            print(emp["name"])
            found = True

    if not found:
        print("No data present")

def distinct_departments(records):
    if not records:
        print("No data present")
        return

    depts = set(emp["department"] for emp in records if emp["department"])

    if not depts:
        print("No data present")
        return

    print("Distinct Departments:")
    for d in depts:
        print(d)

def add_multiple_employees(records, *employees):
    for emp in employees:
        add_employee(records, *emp)

def backup_records(records):
    return copy.deepcopy(records)

def menu():
    records = []

    while True:
        print(" ---------------------Employee Work Analysis---------------------- ")
        print("1. Add Employee")
        print("2. Show Total Hours by Department")
        print("3. Employees Above Certain Hours")
        print("4. Show Distinct Departments")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            hours = input("Enter Hours Worked: ")
            add_employee(records, name, dept, hours)

        elif choice == "2":
            total_hours_by_department(records)

        elif choice == "3":
            try:
                threshold = float(input("Enter minimum hours: "))
                employees_above_hours(records, threshold)
            except:
                print("Invalid input")

        elif choice == "4":
            distinct_departments(records)

        elif choice == "5":
            print("Exiting program safely...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()