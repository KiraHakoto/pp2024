from datetime import datetime
from pw4.domains import Student, Course, Mark

def input_students(school:
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students <= 0:
                print("The number of students must be a positive integer.")
                continue
            for i in range(num_students)
                print(f"Enter information for student {i+1}:")
                id = input("Enter student id: ")
                name = input("Enter student name: ")
                while True:
                    dob = input("Enter student DoB (dd/mm/yyyy): ")
                    try:
                        day, month, year = map(int, dob.split('/'))
                        datetime.datetime(year, month, day)
                        break
                    except ValueError:
                        print("Invalid date. Please enter a valid date format dd/mm/yyyy.")
                student = Student(id, name, dob)
                school.students.append(student)
            break
        except ValueError(
            print("The number of students must be a positive integer.")

def input_courses(school,
    while True:
        try:
            num_courses = int(input("Enter number of courses: ")
            if num_courses <= 0:
                print("The number of courses must be a positive integer.")
                continue
            for i in range(num_courses(
                id = input("Enter course id: ")
                name = input("Enter course name: ")
                credits = int(input("Enter course credits: ")
                course = Course(id, name, credits)
                school.courses.append(course)
            break
        except ValueError(
            print("The number of courses must be a positive integer.")

def input_marks(school, course_id(
    for student in school.students(
        mark = float(input(f"Enter mark for student {student.id} in course {course_id}: ")
        student.add_mark(course_id, mark)

def input_data(school(
    input_students(school)
    input_courses(school)
    input_marks(school, "1001")
    input_marks(school, "1002")
    input_marks(school, "1003")
    input_marks(school, "1004")

if __name__ == "__main__":    input_data(school)