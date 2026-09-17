from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address.")
        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"


class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def role_info(self):
        return f"{self.name} is a Student."

    def __str__(self):
        return (
            f"Student: {self.name}, "
            f"Email: {self.email}, "
            f"ID: {self.student_id}"
        )


class Lecturer(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def role_info(self):
        return f"{self.name} is a Lecturer of {self.subject}."

    def __str__(self):
        return (
            f"Lecturer: {self.name}, "
            f"Email: {self.email}, "
            f"Subject: {self.subject}"
        )


class Course:
    def __init__(self, course_name, lecturer):
        self.course_name = course_name
        self.lecturer = lecturer
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Only Student objects can be added.")

    def __str__(self):
        return (
            f"Course: {self.course_name}, "
            f"Lecturer: {self.lecturer.name}, "
            f"Students: {len(self.students)}"
        )


# Create objects
student1 = Student(
    "Adnan",
    "adnan@gmail.com",
    101
)

student2 = Student(
    "Ahmad",
    "ahmad@gmail.com",
    102
)

lecturer1 = Lecturer(
    "Mr. Ali",
    "ali@university.edu",
    "Python"
)


# Composition
course1 = Course(
    "Python Programming",
    lecturer1
)

course1.add_student(student1)
course1.add_student(student2)


# Polymorphism
people = [
    student1,
    student2,
    lecturer1
]

print("----- People Information -----")

for person in people:
    print(person)
    print(person.role_info())
    print()


print("----- Course Information -----")
print(course1)

print("\nStudents in Course:")

for student in course1.students:
    print(student)