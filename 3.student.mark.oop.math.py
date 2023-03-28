import math
import curses
import numpy 
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_marks(self, course_id):
        return self.marks.get(course_id, None)

    def get_gpa(self, course_weights):
        total_weighted_score = 0
        total_weight = 0
        for course_id, mark in self.marks.items():
            course_weight = course_weights.get(course_id, 0)
            total_weighted_score += mark * course_weight
            total_weight += course_weight
        if total_weight == 0:
            return None
        else:
            return total_weighted_score / total_weight

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def add_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def get_marks(self, student_id):
        return self.marks.get(student_id, None)

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, id, name, dob):
        self.students[id] = Student(id, name, dob)

    def add_course(self, id, name):
        self.courses[id] = Course(id, name)

    def get_student(self, id):
        return self.students.get(id)

    def get_course(self, id):
        return self.courses.get(id)

    def input_student_marks(self):
        course_id = input("Enter the course ID: ")
        course = self.get_course(course_id)
        if not course:
            print("Invalid course ID")
            return
        for student_id, student in self.students.items():
            marks = input(f"Enter marks for {student.name} ({course.name}): ")
            try:
                marks = float(marks)
                marks = math.floor(marks * 10) / 10
            except ValueError:
                print("Invalid input for marks")
                continue
            student.add_mark(course_id, marks)
            course.add_mark(student_id, marks)

    def list_courses(self):
        print("Courses:")
        for course in self.courses.values():
            print(f"{course.id} - {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students.values():
            print(f"{student.id} - {student.name} - {student.dob}")

    def show_student_marks(self):
        course_id = input("Enter the course ID: ")
        course = self.get_course(course_id)
        if not course:
            print("Invalid course ID")
            return
        print(f"Student marks for {course.name}:")
        for student in self.students.values():
            marks = student.get_marks(course_id)
            if marks is not None:
                print(f"{student.name} - {marks}")

    def add_students(self):
        num_students = int(input("Enter the number of students to add: "))
        for i in range(num_students):
            id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student's date of birth (DD/MM/YYYY): ")
            self.add_student(id, name, dob)

    def add_courses(self):
        num_courses = int(input("Enter the number of courses to add: "))
        for i in range(num_courses):
            id = input("Enter the course ID: ")
            name = input("Enter the course name: ")
            self.add_course(id, name)

    def show_student_gpa(self):
        course_weights = {}
        for course in self.courses.values():
            weight = input(f"Enter the weight for {course.name}: ")
            try:
                weight = float(weight)
            except ValueError:
                print("Invalid input for weight")
                return
            course_weights[course.id] = weight
        for student in self.students.values():
            gpa = student.get_gpa(course_weights)
            if gpa is not None:
                print(f"{student.name} - {gpa}")
        
school = School()
while True:
    
    print("1. Add students")
    print("2. Add courses")
    print("3. Input student marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show student marks")
    print("7. Show student GPA")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        school.add_students()
    elif choice == "2":
        school.add_courses()
    elif choice == "3":
        school.input_student_marks()
    elif choice == "4":
        school.list_students()
    elif choice == "5":
        school.list_courses()
    elif choice == "6":
        school.show_student_marks()
    elif choice == "7":
        school.show_student_gpa()
    elif choice == "8":
        break
    else:
        print("Invalid choice")
    



ssss
