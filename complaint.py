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
MULTIPLES_CHOICES = ["a", "b", "c"]

UNITES = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


class Complaint:
    def __init__(self):
        self.unit_number = input("Which unit is your complaint related to it? ")
        self.convert_unit_number()
        self.issue_section = None
        self.complaint_part()
        self.issue_details = None
        self.proof_one = None
        self.proof_two = None
        self.more_details()

    def complaint_part(self):
        is_right = True
        while is_right:
            issue_part = input(
                "Which part do you want to complain about it?\n"
                "A- Discussion forum\n"
                "B- Written Assignment\n"
                "C- Learning Journal\n"
            ).lower()
            if issue_part in MULTIPLES_CHOICES:
                self.issue_section = ASSIGNMENTS_SECTION[issue_part]
                is_right = False
            else:
                print("Please choose from A,B or C : ")

    def more_details(self):
        is_right = True
        while is_right:
            issue_point = input(
                "Why do you want to complain?\n"
                "A- unfairly graded\n"
                "B-Offensive comment\n"
                "C- Others\n"
            ).lower()
            if issue_point in MULTIPLES_CHOICES:
                self.issue_details = USER_ISSUES[issue_point]
                self.proof_questions()
                is_right = False
            else:
                print("Please choose from A,B or C : ")

    def proof_questions(self):
        if self.issue_details == "unfairly graded":
            self.proof_one = input(
                "Would you please give more details why you think you unfairly graded?\n"
                "Example - Mine peer-graded me with the low grades without any feedback.\n"
            )
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

    def convert_unit_number(self):
        if int(self.unit_number) in UNITES:
            self.unit_number = UNITES[int(self.unit_number)]
