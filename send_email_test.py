import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

gmail_user = os.getenv("GMAIL_USER")
gmail_password = os.getenv("GMAIL_PASSWORD")
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email(to_email, subject, message, cc_email=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = gmail_user
        msg["To"] = to_email
        msg["Subject"] = subject
        if cc_email:
            msg["Cc"] = cc_email
            recipients = [to_email, cc_email]
        else:
            recipients = [to_email]
        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipients, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to_email} with subject '{subject}'.")
    except Exception as e:
        print(f"Email sending failed: {e}")

# Example usage:
send_email(
    to_email="recipient@example.com",      # Change to your test email
    subject="Test Email from Jarvis",
    message="Hello, this is a test email sent from your Jarvis assistant!",
    cc_email=None
)