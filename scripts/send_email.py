import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os

def send_email(subject, body_html, to_email="0008leil@gmail.com"):
    from_email = "0008leil@gmail.com"
    password = os.environ.get("GMAIL_APP_PASSWORD", "cxxnrfmiamooiqsj")

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f"Claude Weekly Report <{from_email}>"
    msg['To'] = to_email

    msg.attach(MIMEText(body_html, 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.send_message(msg)

    print(f"Email sent to {to_email}")

if __name__ == "__main__":
    subject = sys.argv[1] if len(sys.argv) > 1 else "Test"
    body = sys.argv[2] if len(sys.argv) > 2 else "<p>Test email from Claude</p>"
    send_email(subject, body)
