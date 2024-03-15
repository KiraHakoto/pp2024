class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def get_info(self):
        return f"{self.id} - {self.name} - {self.dob}"

    def calculate_gpa(self):
        return 0.0