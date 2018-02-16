import cv2
import json
import requests
from config import token, chat_id


TELEGRAM_API = 'https://api.telegram.org/bot' + token

def send_message():
    image_name = 'telegram.png'

    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    _, image = camera.read()
    cv2.imwrite(image_name, image)

    data = {'chat_id': chat_id}
    files = {'photo': (image_name, open(image_name, 'rb'))}
    response = requests.post(TELEGRAM_API + '/sendPhoto', data=data, files=files)
    print response

def main():
    send_message()

if __name__ == '__main__':
    main()