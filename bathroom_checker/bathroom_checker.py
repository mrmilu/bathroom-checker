#!/usr/bin/env python3
import pystray
import requests
from PIL import Image
from time import sleep
from threading import Thread
import os

endpoint = "http://bathroom.mrmilu.com/api/bathroom_updates/1"
resources = {
    "empty": os.path.join(os.path.dirname(__file__), "images/empty.jpg"),
    "busy" : os.path.join(os.path.dirname(__file__), "images/busy.jpg")
}

def icon_setup(icon):
    icon.visible = True
    t = Thread(target=checker, args=(icon,))
    t.start()

def checker(icon):
    while True:
        if is_busy():
            icon.icon = Image.open(resources["busy"])
        else:
            icon.icon = Image.open(resources["empty"])
        sleep(1)

def is_busy():
    request = requests.get(endpoint)
    data = request.json()
    return data["occupied"]


def main():
    icon = pystray.Icon('bathroom_icon')
    icon.icon = Image.open(resources["empty"])
    icon.run(icon_setup)

if __name__ == "__main__":
    main()
