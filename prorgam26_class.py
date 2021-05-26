class Student:


    def __init__(self, roll, name, gpa):
        self.roll = roll
        self.name = name
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, GPA: {self.gpa}")

student1 = Student(101, "John", 3.75)
student1.display()
print(isinstance(student1, Student))



