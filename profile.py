import pandas as pd

class Profile:
    def __init__(self):
        self.student_name = input("Write your first and last name, please : ").title()
        self.instructor_name = input("What is your instructor name : ").title()
        self.group_number = input("What is your group number?")
        self.course_name = input("Which course are you currently doing? ").upper()

    def create_profile(self):
        data = {}
        data["Name"] = [self.student_name]
        data["Instructor name"] = [self.instructor_name]
        data["Group number"] = [self.group_number]
        data["Course Name"] = [self.course_name]
        df = pd.DataFrame(data)
        df_csv = df.to_csv(f"{self.student_name}.csv")