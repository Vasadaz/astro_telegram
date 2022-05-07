import os
import time
from pathlib import Path

import telegram


def send_img_telegram(dirs_img_list: list):
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_pause = os.getenv("TELEGRAM_PAUSE", default=86400)
    chat_id = os.environ["TELEGRAM_CHAT"]
    bot = telegram.Bot(telegram_token)

    while True:
        for name_dur in dirs_img_list:
            path_all_img = os.walk(name_dur)

            for dir in path_all_img:
                for file in dir[2]:
                    path_img = Path(dir[0], file)

                    try:
                        bot.send_photo(chat_id=chat_id, photo=open(path_img, 'rb'))
                        time.sleep(int(telegram_pause))
                    except telegram.error.BadRequest as error_text:
                        print(error_text, path_img)
