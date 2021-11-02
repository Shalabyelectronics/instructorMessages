ASSIGNMENTS_SECTION = {
    "a": "Discussion forum",
    "b": "Written Assignment",
    "c": "Learning Journal"
}
USER_ISSUES = {
    "a": "unfairly graded",
    "b": "Offensive comment",
    "c": "Others"
}


class Complaint():
    def __init__(self):
        self.student_name = input("Write your first and last name, please : ").title()
        self.instructor_name = input("What is your instructor name : ").title()
        self.course_name = input("Which course are you currently doing? ").title()
        self.unit_number = input("Which unit is your complaint related to it? ")
        self.group_number = input("What is your group number?")
        self.complaint_part = input(
            "Which part do you want to complain about it?\n"
            "A- Discussion forum\n"
            "B- Written Assignment\n"
            "C- Learning Journal\n"
        )
        self.issue = input(
            "Why do you want to complain?\n"
            "A- unfairly graded\n"
            "B-Offensive comment\n"
            "C- Others\n"
        )
