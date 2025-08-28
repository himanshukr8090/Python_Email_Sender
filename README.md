# 📧 Python Email Sender

A simple Python script to send emails using Gmail's SMTP server.

---

## ✨ Features
✅ Send plain text emails via Gmail's SMTP server  
✅ Secure connection using TLS  
✅ Basic error handling  
✅ Efficient resource management  

---

## ⚙️ Prerequisites
- 🐍 Python 
- ✉️ A Gmail account
- 🔑 App password (if 2FA is enabled)

---

## 🔧 Setup
1️⃣ Clone this repository or copy the script.  
2️⃣ Ensure you have Python installed (no additional packages required beyond the standard library).  
3️⃣ Configure your email settings.  

---

## 🛠 Configuration
Edit the following variables in the script:

```python
sender_email = "your_email@gmail.com"  # Your Gmail address
receiver_email = "recipient_email@gmail.com"  # Recipient's email
password = "your_app_password"  # Your Gmail password or app password
```

---

📩 The script will:
- Connect to Gmail's SMTP server
- Authenticate using your credentials
- Send a test email
- Print a success or error message

---

## 🔒 Security Best Practices
⚠️ **Never commit your actual password to version control.**  
🔹 Enable **2FA** on your Gmail account.  
🔹 Use an **app-specific password** if 2FA is enabled.  

---

## ⚠️ Error Handling
The script is designed to manage common errors, including:
- ❌ Authentication failures
- 🔌 Connection issues
- 📭 SMTP exceptions

---

## 🎨 Customization
You can easily modify:
🎯 Email subject and body  
📬 Recipient address  
📡 SMTP server details (for other email providers)  
