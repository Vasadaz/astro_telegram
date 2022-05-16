import os
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv


def send_img_telegram(token: str, pause: int, chat_id: str, dirs_img_list: list):
    bot = telegram.Bot(token)

    for name_dir in dirs_img_list:
        for root, dirs, files in os.walk(name_dir):
            for file in files:
                path_img = Path(root, file)

                try:
                    with open(path_img, 'rb') as img:
                        bot.send_photo(chat_id=chat_id, photo=img)
                    time.sleep(pause)
                except telegram.error.BadRequest as error_text:
                    print(error_text, path_img)

                os.remove(path_img)
        os.rmdir(name_dir)


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_pause = int(os.getenv("TELEGRAM_PAUSE", default=86400))
    chat_id = os.environ["TELEGRAM_CHAT"]

    names_dirs = os.listdir()
    img_dirs_list = []

    for name_dir in names_dirs:
        if "images" in name_dir:
            img_dirs_list.append(name_dir)

    send_img_telegram(telegram_token, telegram_pause, chat_id, img_dirs_list)
