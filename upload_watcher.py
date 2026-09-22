import time
import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ⚠️ અહીં તમારા Telegram Bot ની details નાખો
BOT_TOKEN = "8998459133:AAFsLmDMz1laD82Skrr2vlqbCHjjC5HKoLQ"
CHAT_ID = "6728940345"

WATCH_FOLDER = r"C:\AutoUpload"
LOG_FILE = os.path.join(WATCH_FOLDER, "uploaded_links.txt")

if not os.path.exists(WATCH_FOLDER):
    os.makedirs(WATCH_FOLDER)


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = event.src_path

        if file_path.endswith(".txt") or file_path.endswith(".tmp"):
            return

        time.sleep(1)

        self.upload_to_telegram(file_path)


    def upload_to_telegram(self, file_path):

        filename = os.path.basename(file_path)

        print(f"[📤] Telegram પર upload થઈ રહી છે: {filename}...")

        # ✅ Correct Telegram API URL
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

        try:

            with open(file_path, "rb") as f:

                files = {
                    "document": f
                }

                data = {
                    "chat_id": CHAT_ID,
                    "caption": f"📁 નવી ફાઇલ અપલોડ થઈ: {filename}"
                }

                response = requests.post(
                    url,
                    data=data,
                    files=files
                ).json()


            if response.get("ok"):

                print("✅ સફળતાપૂર્વક Telegram પર upload થયું!")
                print("📱 તમારી Telegram એપ ચેક કરો.")

                with open(LOG_FILE, "a", encoding="utf-8") as log:

                    log.write(
                        f"ફાઇલ: {filename} -> Telegram પર મોકલી દેવાઈ.\n"
                    )

            else:

                print(
                    f"❌ Telegram API ભૂલ: "
                    f"{response.get('description')}"
                )


        except Exception as e:

            print(f"❌ અપલોડ કરવામાં સમસ્યા આવી: {e}")


if __name__ == "__main__":

    print(
        f"👁️ Telegram Auto-Uploader ચાલુ છે..."
    )

    print(
        f"📁 Files અહીં મુકો: {WATCH_FOLDER}"
    )

    event_handler = FileHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        path=WATCH_FOLDER,
        recursive=False
    )

    observer.start()

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()
