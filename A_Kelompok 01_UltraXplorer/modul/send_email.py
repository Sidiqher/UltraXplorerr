import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os

def send_png_email(receiver_email, png_file_path):
    
    sender_email = os.environ.get('DB_USER')
    sender_password = os.environ.get('DB_PASS')
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Inisialisasi objek MIMEMultipart
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "ID Card UltraXplorer"

    # Baca file PNG
    with open(png_file_path, 'rb') as file:
        image_data = file.read()

    # Buat objek MIMEImage
    image = MIMEImage(image_data, name='image.png')
    
    # Tambahkan objek MIMEImage ke objek MIMEMultipart

    # Menambahkan isi pesan
    body = """
Hai! Terima kasih telah menggunakan program UltraXplorer. Berikut merupakan hasil cetak ID Card!!

————
UltraXplorer"""
    message.attach(MIMEText(body, 'plain'))
    message.attach(image)

    # Mengirim email menggunakan SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
