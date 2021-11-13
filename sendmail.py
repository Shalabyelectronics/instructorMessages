from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl



class Sendmail:
    def __init__(self):
        self.subject = input("Type your subject title here and hit enter: ").lower()
        self.body = None
        self.sender_email = "complaintmessagegenerator@gmail.com"
        self.receiver_email = input("Type your instructor email and hit enter: ")
        self.password = input("Type your password and press enter:")
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = self.subject
        self.message["Bcc"] = self.receiver_email
        self.message.attach(MIMEText(self.body, "plain"))
        self.filename = "document.pdf"
        self.prapare_email()


    def prapare_email(self):

        with open(self.filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {self.filename}",
        )

        # Add attachment to message and convert message to string
        self.message.attach(part)
        text = self.message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, text)



