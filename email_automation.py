import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

def send_email(sender_email, recipient_email, subject, message, password):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Initialize the SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        print(e)

if __name__ == "__main__":
    # Input sender's email, password, recipient's email, subject, and message
    sender_email = input("Enter your email address: ")
    password = getpass("Enter your email password (hidden): ")
    recipient_email = input("Enter recipient's email address: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")

    # Send email
    send_email(sender_email, recipient_email, subject, message, password)
