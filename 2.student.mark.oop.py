import datetime

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_info(self):
        return f"ID: {self.id}, Name: {self.name}"

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob

    def get_info(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        while True:
            try:
                num_students = int(input("Enter number of students: "))
                if num_students <= 0:
                    print("The number of students must be a positive integer.")
                    continue
                for i in range(num_students):
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
                    self.students.append(Student(id, name, dob))
                break
            except ValueError:
                print("The number of students must be a positive integer.")

    def input_courses(self):
        while True:
            try:
                num_courses = int(input("Enter number of courses: "))
                if num_courses <= 0:
                    print("The number of courses must be a positive integer.")
                    continue
                for i in range(num_courses):
                    id = input("Enter course id: ")
                    name = input("Enter course name: ")
                    self.courses.append(Course(id, name))
                break
            except ValueError:
                print("The number of courses must be a positive integer.")

    def input_marks(self):
        course_id = input("Select a course by id: ")
        course = next((course for course in self.courses if course.id == course_id), None)
        if not course:
            print("There is no course that has this ID.")
            return
        for i, student in enumerate(self.students):
            mark = float(input(f"Enter mark for student {i+1} ({student.name}) in course {course_id}: "))
            self.marks.append(Mark(student, course, mark))

    def list_courses(self):
        for course in self.courses:
            print(course.name)

    def list_students(self):
        for student in self.students:
            print(student.get_info())

    def show_marks(self, course_id):
        for mark in self.marks:
            if mark.course.id == course_id:
                print(f"Mark for student {mark.student.name} in course {mark.course.name}: {mark.mark}")

def main():
    school = School()
    school.input_students()
    school.input_courses()
    school.input_marks()
    school.list_courses()
    school.list_students()
    course_id = input("Enter course id to show marks: ")
    school.show_marks(course_id)

if __name__ == "__main__":
    main()
