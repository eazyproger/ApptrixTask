import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image


def add_photo_watermark(input_image_path, email):
    base_image = Image.open(input_image_path)
    watermark = Image.open('acquaintances/avatars/watermark.png')
    output_image_path = 'acquaintances/avatars/' + email + '.png'
    watermark_position = (base_image.width - watermark.width, base_image.height - watermark.height)
    transparent = Image.new('RGBA', base_image.size, (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, watermark_position, mask=watermark)
    transparent.save(output_image_path)
    return output_image_path


def send_message(email, name):
    address_from = 'apptrixtaskmail@gmail.com'
    password = 'qwertyG!'
    address_to = email
    body = 'Вы понравились ' + name + '! Вот его почта: ' + email

    message = MIMEMultipart()
    message['From'] = address_from
    message['To'] = address_to
    message['Subject'] = 'Вы кому-то понравились!'
    message.attach(MIMEText(body))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(address_from, password)
    server.send_message(message)
    server.quit()
