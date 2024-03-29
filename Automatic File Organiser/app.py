import os
import shutil
import pywintypes
from win10toast import ToastNotifier
from time import sleep

# you can change folder here
folder = os.getcwd()

# You can add more file formats here
image_formats = ["jpg", "png", "jpeg", "gif", "webp", "tiff"]
audio_formats = ["mp3", "wav"]
video_formats = ["mp4", "avi", "webm"]
docs_formats = ["ai", "ait", "txt", "rtf", "pdf", "doc"]
html = ["html"]


def init():
    if not os.path.isdir(os.path.join(folder, "images")):
        os.mkdir(os.path.join(folder, "images"))
    if not os.path.isdir(os.path.join(folder, "audio")):
        os.mkdir(os.path.join(folder, "audio"))
    if not os.path.isdir(os.path.join(folder, "videos")):
        os.mkdir(os.path.join(folder, "videos"))
    if not os.path.isdir(os.path.join(folder, "docs")):
        os.mkdir(os.path.join(folder, "docs"))
    if not os.path.isdir(os.path.join(folder, "others")):
        os.mkdir(os.path.join(folder, "others"))
    if not os.path.isdir(os.path.join(folder, "html")):
        os.mkdir(os.path.join(folder, "html"))


toast = ToastNotifier()
toast.show_toast("File Organiser", "The process has been started", duration=30)


init()
while True:
    files = os.listdir(folder)

    for file in files:
        if os.path.isfile(file) and file != "app.py":
            ext = (file.split(".")[-1]).lower()

            if ext in image_formats:
                shutil.move(file, f"images/{file}")
            elif ext in audio_formats:
                shutil.move(file, f"audio/{file}")
            elif ext in video_formats:
                shutil.move(file, f"videos/{file}")
            elif ext in docs_formats:
                shutil.move(file, f"docs/{file}")
            elif ext in html:
                shutil.move(file, f"html/{file}")
            else:
                shutil.move(file, f"others/{file}")
    del files
    sleep(15)  # if program is using too much memory increae the value of sleep function
