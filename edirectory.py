employees = {
    1001: {"name": "Alice", "job": "Engineer"},
    1002: {"name": "Bob", "job": "Marketing"},
}

# SECTION 1
print("Current Employees:")
for emp_id, info in employees.items():
    print(emp_id, info["name"], "-", info["job"])

# SECTION 2
new_id = int(input("Enter new employee ID: "))
new_name = input("Enter new employee name: ")
new_job = input("Enter new employee job: ")
employees[new_id] = {"name": new_name, "job": new_job}

# SECTION 3
print("\nUpdated Employees:")
for emp_id, info in employees.items():
    print(emp_id, info["name"], "-", info["job"])
