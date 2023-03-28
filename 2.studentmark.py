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
            marks = int(input(f"Enter marks for {student.name} ({course.name}): "))
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

    def show_course_students(self):
        course_id = input("Enter the course ID: ")
        course = self.get_course(course_id)
        if not course:
            print("Invalid course ID")
            return
        print(f"Students and their marks for {course.name}:")
        for student in self.students.values():
            marks = student.get_marks(course_id)
            print(f"{student.name} - {marks}")

school = School()

while True:
    print("1. Add student")
    print("2. Add course")
    print("3. Add students")
    print("4. Add courses")
    print("5. List students")
    print("6. List courses")
    print("7. Input student marks")
    print("8. Show student marks")
    print("9. Show course students")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        id = input("Enter the student ID: ")
        name = input("Enter the student name: ")
        dob = input("Enter the student's date of birth (DD/MM/YYYY): ")
        school.add_student(id, name, dob)
    elif choice == "2":
        id = input("Enter the course ID: ")
        name = input("Enter the course name: ")
        school.add_course(id, name)
    elif choice == "3":
        school.add_students()
    elif choice == "4":
        school.add_courses()
    elif choice == "5":
        school.list_students()
    elif choice == "6":
        school.list_courses()
    elif choice == "7":
        school.input_student_marks()

    elif choice == "8":
        school.show_student_marks()
    elif choice == "9":
        school.show_course_students()
    elif choice == "0":
        break
    else:
        print("Invalid choice")
        
          
