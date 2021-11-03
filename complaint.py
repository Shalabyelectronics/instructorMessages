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


class Complaint:
    def __init__(self):
        self.student_name = input("Write your first and last name, please : ").title()
        self.instructor_name = input("What is your instructor name : ").title()
        self.course_name = input("Which course are you currently doing? ").title()
        self.unit_number = input("Which unit is your complaint related to it? ")
        self.group_number = input("What is your group number?")
        self.issue_section = None
        self.complaint_part()
        self.issue_details = None
        self.proof_one = None
        self.proof_two = None
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

        else:
            print("Please choose from A,B or C : ")

    def more_details(self):
        issue_point = input(
            "Why do you want to complain?\n"
            "A- unfairly graded\n"
            "B-Offensive comment\n"
            "C- Others\n"
        ).lower()
        if issue_point == "a" or issue_point == "b" or issue_point == "c":
            self.issue_details = USER_ISSUES[issue_point]
            self.proof_questions()
        else:
            print("Please choose from A,B or C : ")

    def proof_questions(self):
        if self.issue_details == "unfairly graded":
            self.proof_one = input(
                "Would you please give more details why you think you unfairly graded?\n"
            )
            print(self.proof_one)
            add_proof = input("Do you want to add another poof for unfairly graded issue?").lower()
            if add_proof == "y" or add_proof == "yes":
                self.proof_two = input(
                    "Would you please give more details why you think you unfairly graded?\n"
                )
        elif self.issue_details == "Offensive comment":
            self.proof_one = input(
                "Who is the student who gives you that offensive comment? Please write his full name : \n"
            ).title()
            add_proof = input("Can you provide the link where the offensive comment is located? ?").lower()
            if add_proof == "y" or add_proof == "yes":
                self.proof_two = input(
                    "Please paste the link here : \n"
                )
            else:
                print("It will be much better if you got the link. So your instructor will take action for this "
                      "student. ")
        else:
            self.issue_details = input("Would you please address what your complaint is?\n")
            add_proof = input(f"Do you want to add another poof for {self.issue_details} ?").lower()
            if add_proof == "y" or add_proof == "yes":
                self.proof_one = input(f"What is your proof about {self.issue_details}")
