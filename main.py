from complaint import Complaint
import time

print("Welcome to complaint center.\n")


open_complaint = input("Do you want to create a complaint letter to your instructor?").lower()
if open_complaint == "y" or open_complaint == "yes":
    print("Ok, then let's create your profile first: ")
    create_complaint = Complaint()
    print("Please wait!!! creating your Complaint message")
    print(create_complaint.student_name)
    print(create_complaint.instructor_name)
    print(create_complaint.course_name)
    print(create_complaint.unit_number)
    print(create_complaint.group_number)
    if create_complaint.issue_section is not None:
        print(create_complaint.issue_section)
    if create_complaint.issue_details is not None:
        print(create_complaint.issue_details)
    if create_complaint.proof_one is not None:
        print(create_complaint.proof_one)
    if create_complaint.proof_two is not None:
        print(create_complaint.proof_two)

