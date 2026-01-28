# Python Email Sender 📧

A simple Python script to send emails using **Gmail SMTP with SSL encryption**.

This project demonstrates how to:

* Use Python’s built-in libraries
* Send secure emails via Gmail
* Understand the SMTP workflow (connect → login → send → close)

---

## 🚀 Features

* Sends plain text emails
* Uses Gmail SMTP (`smtp.gmail.com`)
* Secure SSL connection
* Beginner-friendly and easy to extend

---

## 🧰 Technologies Used

* Python 3
* `smtplib`
* `ssl`
* `email.message.EmailMessage`

(All libraries are built into Python — no installation needed)

---

## 📂 Project Structure

```
python-email-sender/
│
├── send_email.py
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

* Python 3 installed
* A Gmail account
* Gmail **App Password** (not your normal password)

---

### 2️⃣ Enable Gmail App Password

1. Go to **Google Account → Security**
2. Enable **2-Step Verification**
3. Create an **App Password**
4. Copy the generated password

---

### 3️⃣ Configure the Script

Open `send_email.py` and update:

```python
sender_email = "your_email@gmail.com"
sender_password = "YOUR_APP_PASSWORD"
receiver_email = "receiver_email@example.com"
```

⚠️ **Never upload real passwords to GitHub**

---

## ▶️ How to Run

```bash
python send_email.py
```

If everything is set correctly, the email will be sent successfully.

---

## 🧠 How It Works

1. Create an email object
2. Add sender, receiver, subject, and body
3. Create a secure SSL connection
4. Login to Gmail SMTP
5. Send the email

---

## 🔐 Security Notes

* Do not hardcode real passwords
* Use `.env` files for sensitive data (recommended for production)
* Never commit secrets to GitHub

---

## 📌 Future Improvements

* HTML email support
* Attachments
* Environment variable support
* Email validation
* CLI arguments

---

## 👤 Author

**Mohammed Taha**

---

## 📄 License

This project is open-source and available for learning and educational purposes.
