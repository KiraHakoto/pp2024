class Course:
    _next_id = 1

    def __init__(self, id, name, credits):
        self.id = id or Course._next_id
        Course._next_id += 1
        self.name = name
        self.credits = credits

    def get_info(self):
        return f"{self.id} - {self.name} - {self.credits} credits"

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.id == other.id
        return False

    def __repr__(self):
        return self.get_info()