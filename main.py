from complaint import Complaint
from profile import Profile
from logo import logo, line
from sendmail import Sendmail
import time

def create_complaint():
    print("Welcome to complaint center.")
    print(logo)

    open_complaint = input("Do you want to create a complaint letter to your instructor?\n"
                           "Please type (y) or (n) : ").lower()
    if open_complaint == "y" or open_complaint == "yes":
        print("Ok, then let's create your profile first: ")
        create_profile = Profile()
        create_complaint = Complaint()

        with open("./letter_of_complaints/test_message.txt", mode="w" ) as test:
                test.write(
                    f"Hello instructor {create_profile.instructor_name},\n"
                    f"My {create_complaint.issue_section} for unit {create_complaint.unit_number} was "
                    f"{create_complaint.issue_details}.\n"
                )

                if create_complaint.proof_one is not None:
                    test.write(f"{create_complaint.proof_one}\n")

                if create_complaint.proof_two is not None:
                    test.write(f"{create_complaint.proof_two}\n")
                test.write(
                    f"I kindly request you check this case out.\n"
                    f"Best regards.\n"
                    f"{create_profile.student_name}.\n"
                    f"Group number : {create_profile.group_number}\n"
                )
        print("Here you are just copy your complaint message.")
        print(line)
        with open("./letter_of_complaints/test_message.txt") as test:
            contents = test.read()
            print(contents)
        send_message = input("Do you want to send it to your instructor now? (yes or no)\n").lower()
        if send_message == "y" or send_message == "yes":
            pass
            # sendemail = Sendmail()
            # sendemail.subject
            # sendemail.body = contents
            # sendemail.receiver_email
            # sendemail.password

        else:
            print("Have a nice day.")

    else:
        print("Have a nice day.")
