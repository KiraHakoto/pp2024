from person import Person
from mark import Mark

class Student(Person):
    def __init__(self, id, name, dob, transcript=None):
        super().__init__(id, name, dob)
        self.transcript = transcript if transcript else []

    def add_mark(self, course, mark):
        self.transcript.append(Mark(self, course, mark))

    def get_transcript(self):
        return self.transcript

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0
        for mark in self.transcript:
            credits = mark.course.credits
            grade = mark.get_grade()
            quality_points = grade.quality_points(credits)
            total_credits += credits
            total_points += grade.points_earned(quality_points)
        return total_points / total_credits

    def get_info(self):
        return f"{self.id} - {self.name} - GPA: {self.calculate_gpa():.2f}"