import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Configuration for email
sender_email = "sendermail@gmail.com"
reciever_eamil = "recievermail@gmail.com"
password = "APP_PASSWORD"

#Create mail
subject = "Test mail from python"
body = "Hello World from python"


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = reciever_eamil
message["Subject"] = subject

#Attatch the body to the mail
message.attach(MIMEText(body, "plain"))

server = None

#Connect to gmail SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    #send the mail
    text = message.as_string()
    server.sendmail(sender_email, reciever_eamil, text)
    print("email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    if server is not None:
        server.quit()
