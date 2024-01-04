# Student's name: Pham Viet Hai Dang
# Student ID:22bi13074
# Practical work 1: student mark management

import datetime

# Initialize data structures
students = []
courses = []
marks = {}

# Input functions
def input_students():
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students <= 0:
                print("Number of students should be greater than 0.")
                continue
            for i in range(num_students):
                print(f"Enter information for student {i+1}:")
                id = input("Enter student id: ")
                name = input("Enter student name: ")
                while True:
                    dob = input("Enter student DoB (dd/mm/yyyy): ")
                    try:
                        # Check if the date is valid
                        day, month, year = map(int, dob.split('/'))
                        datetime.datetime(year, month, day)
                        break
                    except ValueError:
                        print("Invalid date. Please enter a valid date format dd/mm/yyyy.")
                students.append((id, name, dob))
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer number.")

def input_courses():
    while True:
        try:
            num_courses = int(input("Enter number of courses: "))
            if num_courses <= 0:
                print("Number of courses should be greater than 0.")
                continue
            for i in range(num_courses):
                print(f"Enter information for course {i+1}:")
                id = input("Enter course id: ")
                name = input("Enter course name: ")
                courses.append((id, name))
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer number.")

def input_marks():
    course_id = input("Select a course by id: ")
    if course_id not in [course[0] for course in courses]:
        print("There is no course that has this ID.")
        return
    for i, student in enumerate(students):
        while True:
            try:
                mark = float(input(f"Enter mark for student {i+1} ({student[1]}) in course {course_id}: "))
                if mark < 0 or mark > 20:
                    print("Mark should be between 0 and 20.")
                    continue
                marks[(student[0], course_id)] = mark
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

# Listing functions
def list_courses():
    for course in courses:
        print(course)

def list_students():
    for student in students:
        print(student)

def show_marks(course_id):
    if course_id not in [course[0] for course in courses]:
        print("There is no course that has this ID in the database.")
        return
    for i, student in enumerate(students):
        print(f"Mark for student {i+1} ({student[1]}) in course {course_id}: {marks.get((student[0], course_id), 'N/A')}")

# Main function to start the program
def main():
    input_students()
    input_courses()
    input_marks()
    list_courses()
    list_students()
    course_id = input("Enter course id to show marks: ")
    show_marks(course_id)

if __name__ == "__main__":
    main()
