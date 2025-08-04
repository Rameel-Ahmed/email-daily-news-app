import smtplib
import ssl

def send_email(message):
    # SMTP server and port for Gmail
    host = "smtp.gmail.com"
    port = 465  # SSL port

    # Sender's email credentials (use app-specific password for Gmail)
    username = "pp8ask@gmail.com"
    password = "puyjaxfejfpxkc"

    # Receiver's email address
    receiver = "pplask@gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect securely to the SMTP server
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)                 # Login to Gmail account
        server.sendmail(username, receiver, message)     # Send email to receiver
