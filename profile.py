import pandas
import pandas as pd


class Profile:
    def __init__(self):
        self.student_name = None
        self.instructor_name = None
        self.group_number = None
        self.course_name = None
        self.check_profile()

    def create_profile(self):
        pass
        # data["Name"] = []
        # data["Instructor name"] = []
        # data["Group number"] = []
        # data["Course Name"] = []
        # df = pd.DataFrame(data)
        # df_csv = df.to_csv("students_data.csv")

    def check_profile(self):
        self.student_name = input("Please, write your first and last name:  ").title()
        students_data = pandas.read_csv("students_data.csv", index_col=0)
        names = students_data["Name"].tolist()
        if self.student_name in names:
            print("We checked that you created a profile before")
            do_check = input("Do you want to check your profile if you want to change any thing before move on :\n"
                             "").lower()
            if do_check == "y" or do_check == "yes":
                print(students_data)
                double_check = input("Do you want to use the same details?\n")
                if double_check == "y" or double_check == "yes":
                    students_dictionary = students_data.to_dict()
                    self.student_name = students_dictionary["Name"][0]
                    self.instructor_name = students_dictionary["Instructor name"][0]
                    self.group_number = students_dictionary["Group number"][0]
                    self.course_name = students_dictionary["Course Name"][0]


        else:
            self.instructor_name = input("What is your instructor name : ").title()
            self.group_number = input("What is your group number?")
            self.course_name = input("Which course are you currently doing? ").upper()
            print("Did not match!!!")

            # print("No")
