import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Загрузка переменных окружения
def send_log_email():
    """Отправляет лог-файл с действиями пользователя на почту."""
    load_dotenv()

    # Настройки SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Получение учетных данных из .env
    username = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    recipient_email = os.getenv("RECEPIENT_EMAIL")

    # Путь к лог-файлу
    log_file_path = "user_action.log"

    # Создание сообщения
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = recipient_email
    msg["Subject"] = "Лог-файл с действиями пользователя"
    msg.attach(MIMEText("Во вложении находится лог-файл с действиями пользователя.", "plain"))

    # Проверка существования файла
    if os.path.exists(log_file_path):
        with open(log_file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(log_file_path)}")
            msg.attach(part)
    else:
        print(f"⚠️ Файл {log_file_path} не найден. Отправка без вложения.")

    # Отправка письма
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Защищенное соединение
            server.login(username, password)  # Авторизация
            server.send_message(msg)  # Отправка письма
            print("✅ Лог-файл успешно отправлен!")
    except Exception as e:
        print(f"❌ Ошибка отправки письма: {e}")

