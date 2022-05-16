import os
import urllib.parse
from datetime import datetime

import requests
from dotenv import load_dotenv

from downloader import download_img


COUNT_IMG_NASA_APOD = 30
COUNT_IMG_NASA_EPIC = 5
DIR_IMG_NASA_APOD = "images_nasa_apod"
DIR_IMG_NASA_EPIC = "images_nasa_epic"


def download_img_apod(token: str, count_img: int, dir_for_img: str):
    payload = {"api_key": token, "count": count_img}
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    for nasa_day in response.json():
        nasa_link_img = nasa_day.get("hdurl")

        if nasa_link_img:
            download_img(nasa_link_img, dir_for_img)


def download_img_epic(token: str, count_img: int, dir_for_img: str):
    payload = {"api_key": token}
    url = "https://api.nasa.gov/EPIC/api/natural"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    epic_img_info_list = response.json()

    for epic_last_img_info in epic_img_info_list[-count_img:]:
        epic_last_img_date_iso = datetime.fromisoformat(epic_last_img_info["date"])
        epic_last_img_date = datetime.strftime(epic_last_img_date_iso, "%Y/%m/%d")
        epic_last_img_name = epic_last_img_info["image"]
        epic_last_img_url = f"https://api.nasa.gov/EPIC/archive/natural/" \
                            f"{epic_last_img_date}/png/{epic_last_img_name}.png?"

        download_img(epic_last_img_url + urllib.parse.urlencode(payload), dir_for_img)


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    nasa_token = os.environ["NASA_TOKEN"]

    download_img_apod(nasa_token, COUNT_IMG_NASA_APOD, DIR_IMG_NASA_APOD)
    download_img_epic(nasa_token, COUNT_IMG_NASA_EPIC, DIR_IMG_NASA_EPIC)
