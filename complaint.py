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
        self.issue_section = "null"
        self.complaint_part()
        self.issue_details = "null"
        self.more_details()

    def complaint_part(self):
        issue_part = input(
            "Which part do you want to complain about it?\n"
            "A- Discussion forum\n"
            "B- Written Assignment\n"
            "C- Learning Journal\n"
        ).lower()
        if issue_part == "a" or issue_part == "b" or issue_part == "c":
            self.issue_section = ASSIGNMENTS_SECTION[issue_part]
            return True
        else:
            print("Please choose from A,B or C : ")
            return False

    def more_details(self):
        issue_point = input(
            "Why do you want to complain?\n"
            "A- unfairly graded\n"
            "B-Offensive comment\n"
            "C- Others\n"
        ).lower()
        if issue_point == "a" or issue_point == "b" or issue_point == "c":
            self.issue_details = USER_ISSUES[issue_point]
            return True
        else:
            print("Please choose from A,B or C : ")
            return False

