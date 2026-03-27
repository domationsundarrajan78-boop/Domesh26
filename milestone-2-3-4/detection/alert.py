import smtplib
from email.mime.text import MIMEText

EMAIL = "domationsundarrajan78@gmail.com"
PASSWORD = "yssbwgyqtvajtewq"

def send_alert(anomalies):
    print("👉 send_alert function called")

    if not anomalies:
        print("⚠️ No anomalies found")
        return

    message = "\n".join([str(log) for log in anomalies])

    msg = MIMEText(message)
    msg["Subject"] = "🚨 Anomaly Alert"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        print("👉 Logging in...")
        server.login(EMAIL, PASSWORD)

        print("👉 Sending email...")
        server.send_message(msg)

        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Email failed:", e)