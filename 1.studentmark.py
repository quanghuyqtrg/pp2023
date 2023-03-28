# Input number of students in a class
def input_num_students():
    return int(input("Enter the number of students in the class: ")) ## input() function is used to take input from the user

# Input student information: id, name, DoB
def input_student_info():
    student_id = input("Enter the student ID: ")
    student_name = input("Enter the student name: ")
    student_dob = input("Enter the student's date of birth (DD/MM/YYYY): ")
    return {"id": student_id, "name": student_name, "dob": student_dob, "marks": {}}

# Input number of courses
def input_num_courses():
    return int(input("Enter the number of courses: "))

# Input course information: id, name
def input_course_info():
    course_id = input("Enter the course ID: ")
    course_name = input("Enter the course name: ")
    return {"id": course_id, "name": course_name, "marks": {}}## marks is a dictionary

# Select a course, input marks for student in that course
def input_student_marks(course):
    for student in students:
        marks = int(input(f"Enter marks for {student['name']} ({course['name']}) : "))
        student["marks"][course["id"]] = marks

# List courses
def list_courses():
    print("Courses:")
    for course in courses:
        print(f"{course['id']} - {course['name']}")

# List students
def list_students():
    print("Students:")
    for student in students:
        print(f"{student['id']} - {student['name']} - {student['dob']}")

# Show student marks for a given course
def show_student_marks(course):
    print(f"Student marks for {course['name']}:")
    for student in students:
        print(f"{student['name']} - {student['marks'][course['id']]}")

# Select a course
def select_course():
    list_courses()
    course_id = input("Enter the course ID: ")
    for course in courses:
        if course["id"] == course_id:
            return course
    print("Invalid course ID")
    return None

# Menu
students = []
courses = []
num_courses = 0
num_students = 0

def menu():
    while True:
        print("1. Input number of students in the class")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Select a course, input mark for student in that course")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a given course")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            num_students = input_num_students()
        elif choice == "2":
            for i in range(num_students):
                students.append(input_student_info())
        elif choice == "3":
            num_courses = input_num_courses()
        elif choice == "4":
            for i in range(num_courses):
                courses.append(input_course_info())
        elif choice == "5":
            course = select_course()
            if course:
                input_student_marks(course)
        elif choice == "6":
            list_courses()
        elif choice == "7":
            list_students()
        elif choice == "8":
            course = select_course()
            if course:
                show_student_marks(course)
        elif choice == "9":
            break
        else:
            print("Invalid choice")

menu()
