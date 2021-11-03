from complaint import Complaint

print("Welcome to complaint center.\n")


open_complaint = input("Do you want to create a complaint letter to your instructor?").lower()
if open_complaint == "y" or open_complaint == "yes" :
    print("Ok, then let's create your profile first: ")
    create_complaint = Complaint()
