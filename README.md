# email-daily-news-app
# Email Sender Script (Python)

This project provides a simple Python function to send emails using Gmail's SMTP server securely over SSL.

## 📌 Features
- Sends plain text email to a specified receiver.
- Uses Gmail's SMTP with SSL for secure communication.
- Easily customizable for different recipients or messages.

## 🛠️ Requirements

- Python 3.x
- `smtplib` and `ssl` (standard libraries; no need to install)
- A Gmail account with **App Passwords** enabled (if 2FA is turned on)

## 🧾 Setup

1. **Enable App Passwords in Gmail:**
   - Go to your Google account settings.
   - Under **Security**, enable **2-Step Verification**.
   - Then generate an **App Password** and use it in place of your Gmail password.

2. **Clone the project or copy the script:**
   ```bash
   git clone https://github.com/Rameel-Ahmed/email-daily-news-app.git
