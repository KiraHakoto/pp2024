from pw4.domains import Student, Course, Mark

def list_courses(school(
    for course in school.courses(
        print(f"{course.id} {course.name} {course.credits}")

def list_students(school(
    for student in school.students(
        print(f"{student.id} {student.name} {student.get_dob_str()}")

def show_marks(school, course_id(
    for student in school.students(
        if student.has_course_marks(course_id):
            print(f"Student {student.id} ({student.name}): [{student.calculate_grade(course_id)}] {student.get_marks_for_course(course_id)}")

if __name__ == "__main__":    show_marks(school, "1001")