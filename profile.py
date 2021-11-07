

class Profile:
    def __init__(self):
        self.student_name = input("Write your first and last name, please : ").title()
        self.instructor_name = input("What is your instructor name : ").title()
        self.course_name = input("Which course are you currently doing? ").upper()

