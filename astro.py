import os

from dotenv import load_dotenv

import nasa
import spacex
import telegram_poster


COUNT_IMG_NASA_APOD = 3
COUNT_IMG_NASA_EPIC = 5
DIR_IMG_NASA_APOD = "images_nasa_apod"
DIR_IMG_NASA_EPIC = "images_nasa_epic"
DIR_IMG_SPACEX = "images_spacex"
DIRS_IMG = [DIR_IMG_SPACEX, DIR_IMG_NASA_APOD, DIR_IMG_NASA_EPIC]


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    nasa_token = os.environ["NASA_TOKEN"]
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_pause = int(os.getenv("TELEGRAM_PAUSE", default=86400))
    telegram_chat_id = os.environ["TELEGRAM_CHAT"]

    while True:
        spacex.download_last_launch_imgs(DIR_IMG_SPACEX)
        nasa.download_imgs_apod(nasa_token, COUNT_IMG_NASA_APOD, DIR_IMG_NASA_APOD)
        nasa.download_imgs_epic(nasa_token, COUNT_IMG_NASA_EPIC, DIR_IMG_NASA_EPIC)
        telegram_poster.send_img_telegram(telegram_token, telegram_pause, telegram_chat_id, DIRS_IMG)
