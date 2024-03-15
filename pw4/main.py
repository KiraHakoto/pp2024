import sys
import input
import output
from pw4.domains.school import School

def main():
    school = School()
    school.students = []
    school.courses = []
    school.marks = []

    input.input_students(school)
    input.input_courses(school)

    print("Number of students: {}\n".format(len(school.students)))
    output.list_students(school)
    print("\n")

    course_id = input("Enter course ID for marks: ")
    output.show_marks(school, course_id)

if __name__ == '__main__':
    main()