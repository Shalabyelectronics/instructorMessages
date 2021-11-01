print("Welcome to complaint center.\n\n")
user_input = input("Do you want to create a complaint letter to your instructor?")
if user_input.lower() == "yes" or user_input.lower() == "y":
    print("Ok, then let's create your profile first: ")
    user_name = input("Write your first and last name, please : ")
    user_course = input("Which course are you currently doing? ")
    user_unit = input("Which unit is your complaint related to it? ")
    # TODO 1 we are going to build a dictionary that holds of courses name and their own code.
    # So I can be sure what the user specific course he is doing.
    user_instructor_name = input("What is your instructor name : ")
    user_complaint_part = input(
        "Which part do you want to complain about it?\n"
        "A- Discussion forum\n"
        "B- Written Assignment\n"
        "C- Learning Journal\n"
    )
    user_issue = input(
        "Why do you want to complain?\n"
        "A- unfairly graded\n"
        "B-Offensive comment\n"
        "C- Others\n"
    )
    if user_issue.lower() == "c":
        user_issue = input("Would you please address what your complaint is?\n")
    elif user_issue.lower() == "b":
        user_issue = input("Who is the student who gives you that offensive comment? ")
        user_issue_link = input(
            "Can you provide the link where the offensive comment is located? "
        )
        if user_issue_link.lower() == "yes" or user_issue_link.lower() == "y":
            user_issue_link = input("Please paste the link here : ")
        else:
            print(
                "It will be much better if you got the link. So your instructor will take action for this student. "
            )
