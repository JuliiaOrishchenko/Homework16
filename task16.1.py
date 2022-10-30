class Person:
    school_name = "Harmony"
    def __init__(self, first_name, last_name, age, address, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.gender = gender

    def is_present(self):
        print("Person is present at school")


class Student(Person):
    def __init__(self, first_name, last_name, age, address, gender, parents_phone, group):
        super().__init__(first_name, last_name, age, address, gender)
        self.parents_phone = parents_phone
        self.group = group

    def do_homework(self):
        print("I pass a homework")

    def choose_subject(self):
        print("I can choose subject")

class Teacher(Person):
    def __init__(self, first_name, last_name, age, address, gender, phone, position, salary):
        super().__init__(first_name, last_name, age, address, gender)
        self.phone = phone
        self.position = position
        self.salary = salary

    def teach(self):
        print("I can teach")

    def check_homework(self, grade):
        print(f"Your grade is {grade}")






