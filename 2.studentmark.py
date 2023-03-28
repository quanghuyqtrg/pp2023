class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, marks):
        self.marks[course_id] = marks

    def get_marks(self, course_id):
        return self.marks.get(course_id, 0)
    
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def add_mark(self, student_id, marks):
        self.marks[student_id] = marks

    def get_marks(self, student_id):
        return self.marks.get(student_id, 0)
class Mark:
    def __init__(self, student, course, marks):
        self.student = student
        self.course = course
        self.marks = marks
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
        for course_id, course in self.courses.items():
            print(f"{course_id} - {course.name}")
    def list_students(self):
        for student_id, student in self.students.items():
            print(f"{student_id} - {student.name}")
    def list_student_marks(self):
        student_id = input("Enter the student ID: ")
        student = self.get_student(student_id)
        if not student:
            print("Invalid student ID")
            return
        for course_id, marks in student.marks.items():
            course = self.get_course(course_id)
            print(f"{course.name} - {marks}")
    def list_course_marks(self):
        course_id = input("Enter the course ID: ")
        course = self.get_course(course_id)
        if not course:
            print("Invalid course ID")
            return
        for student_id, marks in course.marks.items():
            student = self.get_student(student_id)
            print(f"{student.name} - {marks}")
    def list_student_average(self):
        student_id = input("Enter the student ID: ")
        student = self.get_student(student_id)
        if not student:
            print("Invalid student ID")
            return
        total = 0
        for marks in student.marks.values():
            total += marks
        print(f"{student.name} - {total / len(student.marks)}")
    def list_course_average(self):
        course_id = input("Enter the course ID: ")
        course = self.get_course(course_id)
        if not course:
            print("Invalid course ID")
            return
        total = 0
        for marks in course.marks.values():
            total += marks
        print(f"{course.name} - {total / len(course.marks)}")

        
       
    

def display_menu():
    print("1. List students")
    print("2. List courses")
    print("3. Add a student")
    print("4. Add a course")
    print("5. Input student marks")
    print("6. List student marks")
    print("7. List course marks")
    print("8. List student average")
    print("9. List course average")
    print("10. Exit")
    print()
def main():

    school = School()
    school.add_student("S01", "John", "1990-01-01")
    school.add_student("S02", "Mary", "1990-02-02")
    school.add_student("S03", "Bob", "1990-03-03")
    school.add_course("C01", "Maths")
    school.add_course("C02", "English")
    school.add_course("C03", "Science")
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            school.list_students()
        elif choice == "2":
            school.list_courses()
        elif choice == "3":
            id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student date of birth (YYYY-MM-DD): ")
            school.add_student(id, name, dob)
        elif choice == "4":
            id = input("Enter the course ID: ")
            name = input("Enter the course name: ")
            school.add_course(id, name)
        elif choice == "5":
            school.input_student_marks()
        elif choice == "6":
            school.list_student_marks()
        elif choice == "7":
            school.list_course_marks()
        elif choice == "8":
            school.list_student_average()
        elif choice == "9":
            school.list_course_average()
        elif choice == "10":
            break
        else:
            print("Invalid choice")
        print()




