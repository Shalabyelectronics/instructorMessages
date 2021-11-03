from complaint import Complaint
from logo import logo
import time

print("Welcome to complaint center.")
print(logo)

open_complaint = input("Do you want to create a complaint letter to your instructor?").lower()
if open_complaint == "y" or open_complaint == "yes":
    print("Ok, then let's create your profile first: ")
    create_complaint = Complaint()
    print("Please wait!!! creating your Complaint message")


    with open("./letter_of_complaints/test_message.txt", mode="w" ) as test:
            test.write(
                f"Hello instructor {create_complaint.instructor_name},\n"
                f"My {create_complaint.issue_section} for unit {create_complaint.unit_number} was "
                f"{create_complaint.issue_details}\n"
            )

            if create_complaint.proof_one is not None:
                test.write(f"{create_complaint.proof_one}\n")

            if create_complaint.proof_two is not None:
                test.write(f"{create_complaint.proof_two}\n")
            test.write(
                f"I kindly request you check this case out.\n"
                f"Best regards.\n"
                f"{create_complaint.student_name}.\n"
                f"Group number : {create_complaint.group_number}\n"
            )



