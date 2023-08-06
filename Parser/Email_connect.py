from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .Create_HTML import create_HTML
from dotenv import load_dotenv
import os
import aiofiles
import aiosmtplib

load_dotenv()


async def send_email(data):
    await create_HTML(data)
    for i in range(len(data)):
        # Адрес электронной почты, которая будет отправлять сообщение
        sender = os.getenv('EMAIL')

        # Адрес электронной почты, на который вы хотите отправить сообщение
        recipient = data[i]['Пошта']

        # Это пароль для созданного приложения в почте
        password = os.getenv('PASSWORD')

        try:
            # Открывает и записываем страничку в - template
            async with aiofiles.open(f"index_{i + 1}.html", encoding='utf-8', mode='r') as file:
                template = await file.read()
        except IOError:
            return "The template"

        message = MIMEMultipart("alternative")
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = "Тестовая тема"
        message.attach(MIMEText(template, "html", "utf-8"))
        await aiosmtplib.send(message, hostname="smtp.gmail.com", port=465, use_tls=True, username=sender,
                              password=password)

        print('Message sent successfully')
