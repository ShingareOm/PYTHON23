class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def read_info(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self):
        super().__init__()
        self.grade = ""

    def read_student_info(self):
        super().read_info()
        self.grade = input("Enter grade: ")

    def print_student_info(self):
        super().print_info()
        print("Grade:", self.grade)


# Example usage:
student = Student()
student.read_student_info()
print("\nStudent Information:")
student.print_student_info()
