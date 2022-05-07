import os

from dotenv import load_dotenv

import nasa
import spacex
import telegram_poster

if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    dirs_for_img_list = ["images_spacex", "images_nasa_apod", "images_nasa_epic"]

    spacex.douwnload_img_last_launch(156, "images_spacex")
    nasa.download_img_apod(5, "images_nasa_apod")
    nasa.download_img_epic(5, "images_nasa_epic")
    telegram_poster.send_img_telegram(dirs_for_img_list)
