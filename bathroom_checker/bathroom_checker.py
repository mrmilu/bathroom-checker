#!/usr/bin/env python3
import pystray
import requests
from PIL import Image
from time import sleep
from threading import Thread
import os
import sys
from shutil import which
from subprocess import run

# support for pyinstaller package
if getattr(sys, 'frozen', False):
    # running in a bundle
    resources = {
        "empty": os.path.join(sys._MEIPASS, "images/empty.jpg"),
        "busy": os.path.join(sys._MEIPASS, "images/busy.jpg")
    }

else:
    # running live
    resources = {
        "empty": os.path.join(os.path.dirname(__file__), "images/empty.jpg"),
        "busy": os.path.join(os.path.dirname(__file__), "images/busy.jpg")
    }

enabled_notifications = False
latest_state = "empty"
endpoint = "http://bathroom.mrmilu.com/api/bathroom_updates/1"

def notificator(message):
    if enabled_notifications:
        if sys.platform == "linux":
            notify2.Notification('Bathroom Checker', message).show()
        elif sys.platform == "darwin":
            run(["terminal-notifier", "-title", 'Bathroom Checker', "-message", message])


def on_clicked(icon, item):
    global enabled_notifications
    enabled_notifications = not item.checked


def icon_setup(icon):
    icon.visible = True
    t = Thread(target=checker, args=(icon,))
    t.start()


def checker(icon):
    global latest_state
    while True:
        if is_busy():
            icon.icon = Image.open(resources["busy"])
            if latest_state != "busy":
                latest_state = "busy"
                notificator("Bathroom busy!")
        else:
            icon.icon = Image.open(resources["empty"])
            if latest_state != "empty":
                latest_state = "empty"
                notificator("Bathroom available!")
        sleep(1)


def is_busy():
    request = requests.get(endpoint)
    data = request.json()
    return data["occupied"]


def terminate(icon):
    os._exit(0)


def main():
    icon_menu = pystray.Menu(*menu_items)
    icon = pystray.Icon('bathroom_icon', menu=icon_menu)
    icon.icon = Image.open(resources["empty"])
    icon.run(icon_setup)


menu_items = []

if ((sys.platform == "darwin" and which("terminal-notifier")) or
    sys.platform == "linux"):
    menu_items.append(pystray.MenuItem("Enable notifications", on_clicked,
        checked=lambda item: enabled_notifications, visible=True))

if sys.platform == "linux":
    import notify2
    notify2.init("Bathroom Notificator")

menu_items.append(pystray.MenuItem("Exit", terminate, visible=True))

if __name__ == "__main__":
    main()
