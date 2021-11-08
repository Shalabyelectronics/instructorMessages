# complaint Messages to instructor version 0.1
### Introduction:
This mini-project will focus on a common problem most online students could face, and it is writing a complaint request to the Instructor.
First, it sounds easy, but it is a massive issue for some students because they couldn't arrange their thoughts to determine their problem.
That is why this project came to solve this problem by generating a specific complaint message to your Instructor.
The main idea of this project is about collecting the primary information from the student then generating a ready message that is a copy-paste only.
### How it's work?
When the code run it will ask the student three types of questions:
* Student details (Group number, First and last name)
* Course details (Course name, unit, and type of assignment section)
* Issue details (unfairly graded, Offensive comment, others)

#### After collecting all this information from the student, the output will be something like this:

Example:
```
Hello instructor [instructor_name],

I'm currently doing [course_name].
My [type of assignment section] for unit [unit number] was [Issue details].

I kindly request you check this case out.

Best regards.
[student  First and last nam]
Group number : [group number]
```
#### This is a simple example provide how the output will look like.
#### So we have nine variables we are going to change as below:
* [instructor_name]
* [course_name]
* [type of assignment section]
* [unit number]
* [Issue details]
* [student First and last nam]
* [group number]
* [user_issue_proof]
* [user_issue_more_details]

##Classes used for:
I created two main classes so far Complaint class and Profile class.
####Complaint class:
I create Complaint class because I need to arrange my main.py file and to handle users input easier,
as it contains all questions needed to create the complaint message, and I'm updating it frequently 
to hold more questions to get much efficient and clear message.
####Profile class:
I create Profile class because I need to create one profile for each user, so I could save more time.
The class has check profile method which check user profile from his name and if it finds the username 
it will ask the user to check his details to be sure about it then use it for the complaint message.
I used Pandas library to help me handle user data.

##Output:

The output file will be a text file type, and it will be located in the letter_of_complaints folder.
Also, student just can copy the message as in the end the program will read the final result.


