class Employee:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.salary = 0.0

    def read_employee_info(self):
        self.name = input("Enter employee name: ")
        self.department = input("Enter department: ")
        self.salary = float(input("Enter salary: "))

    def print_employee_info(self):
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

# Example usage:
employee = Employee()
employee.read_employee_info()
print("\nEmployee Information:")
employee.print_employee_info()
