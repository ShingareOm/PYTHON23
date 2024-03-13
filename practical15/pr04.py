class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student:
    def __init__(self, student_id):
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)


class Resident(Person, Student):
    def __init__(self, name, age, student_id, city):
        Person.__init__(self, name, age)
        Student.__init__(self, student_id)
        self.city = city

    def display_resident(self):
        print("City:", self.city)


# Example usage:
resident = Resident("John", 25, "2021001", "New York")
resident.display_person()
resident.display_student()
resident.display_resident()
