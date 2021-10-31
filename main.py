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
    user_complaint_part = input("Which part do you want to complain about it?\n"
                                "A- Discussion forum\n"
                                "B- Written Assignment\n"
                                "C- Learning Journal\n")
    user_issue = input("Why do you want to complain?\n"
                       "A- unfairly graded\n"
                       "B-Offensive comment\n"
                       "C- Others\n")


