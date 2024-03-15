from datetime import datetime

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def get_date(self):
        return datetime.now()

    def get_grade(self):
        return 'N/A'