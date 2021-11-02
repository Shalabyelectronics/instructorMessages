

print("Welcome to complaint center.\n")


def proceed():
    user_input = input("Do you want to create a complaint letter to your instructor?")
    if user_input.lower() == "yes" or user_input.lower() == "y":
        return True
    return False


def multiple_choices_checker(x, question):
    if x.lower() == "a" or x.lower() == "b" or x == "c":
        question = question[x]
        return question


def yes_no_checker(x):
    if x.lower() == "y" or x.lower() == "n":
        return True


if proceed():
    print("Ok, then let's create your profile first: ")
    user_full_name = input("Write your first and last name, please : ")
    user_course = input("Which course are you currently doing? ")
    user_unit = input("Which unit is your complaint related to it? ")
    user_instructor_name = input("What is your instructor name : ")
    user_group_number = input("What is your group number?")
    is_true = False
    while not is_true:
        user_complaint_part = input(
            "Which part do you want to complain about it?\n"
            "A- Discussion forum\n"
            "B- Written Assignment\n"
            "C- Learning Journal\n"
        )
        is_true = multiple_choices_checker(x=user_complaint_part, question=ASSIGNMENTS_SECTION)
        if not is_true:
            print("Please choose from A,B or C : ")

    is_true = False
    while not is_true:
        user_issue = input(
            "Why do you want to complain?\n"
            "A- unfairly graded\n"
            "B-Offensive comment\n"
            "C- Others\n"
        )
        is_true = multiple_choices_checker(user_issue, USER_ISSUES)
        if not is_true:
            print("Please choose from A,B or C : ")
        else:
            if user_issue.lower() == "c":
                user_issue = input("Would you please address what your complaint is?\n")
            elif user_issue.lower() == "b":
                user_issue = input("Who is the student who gives you that offensive comment? ")
                user_issue_proof = input(
                    "Can you provide the link where the offensive comment is located? "
                )
                if user_issue_link.lower() == "yes" or user_issue_link.lower() == "y":
                    user_issue_link = input("Please paste the link here : ")
                else:
                    print(
                        "It will be much better if you got the link. So your instructor will take action for this "
                        "student. "
                    )
            elif user_issue.lower() == "a":
                user_issue_more_details = input("Would you please give more details why you think you unfairly "
                                                "graded?\n")
        print(f"user_instructor_name : {user_instructor_name}")
        print(f"user_full_name : {user_full_name}")
        print(f"user_course : {user_course}")
        print(f"Group number : {user_group_number}")
        print("user_unit" + " " + str(user_unit))
        print(f"ASSIGNMENTS_SECTION {ASSIGNMENTS_SECTION[user_complaint_part]}")
        print(f"USER_ISSUE : {USER_ISSUES[user_issue]}")
        print(f"user_issue_more_details {user_issue_more_details}")

else:
    print("You did not want to proceed")
