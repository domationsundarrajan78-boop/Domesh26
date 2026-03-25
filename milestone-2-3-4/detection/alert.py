import smtplib
from email.mime.text import MIMEText

EMAIL = "domationsundarrajan78@gmail.com"
PASSWORD = "eoxygzmrgvxfhypo"

def send_alert(anomalies):
    print("👉 send_alert function called")   # DEBUG

    if not anomalies:
        print("⚠️ No anomalies found, email not sent")
        return

    message = "\n".join([str(log) for log in anomalies])

    msg = MIMEText(message)
    msg["Subject"] = "🚨 Anomaly Report (First 100 Logs)"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        print("👉 Logging in...")   # DEBUG
        server.login(EMAIL, PASSWORD)

        print("👉 Sending email...")  # DEBUG
        server.send_message(msg)

        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Email failed:", e)