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


def download_imgs_apod(token: str, count_img: int, dir_for_img: str):
    payload = {"api_key": token, "count": count_img}
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    for day in response.json():
        img_url = day.get("hdurl")

        if img_url:
            download_img(img_url, dir_for_img)


def download_imgs_epic(token: str, count_img: int, dir_for_img: str):
    payload = {"api_key": token}
    url = "https://api.nasa.gov/EPIC/api/natural"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    imgs = response.json()

    for last_img in list(reversed(imgs))[:count_img]:
        iso_date = datetime.fromisoformat(last_img["date"])
        last_img_date = datetime.strftime(iso_date, "%Y/%m/%d")
        img_name = last_img["image"]
        img_url = f"https://api.nasa.gov/EPIC/archive/natural/" \
                            f"{last_img_date}/png/{img_name}.png?"

        download_img(img_url + urllib.parse.urlencode(payload), dir_for_img)


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    nasa_token = os.environ["NASA_TOKEN"]

    download_imgs_apod(nasa_token, COUNT_IMG_NASA_APOD, DIR_IMG_NASA_APOD)
    download_imgs_epic(nasa_token, COUNT_IMG_NASA_EPIC, DIR_IMG_NASA_EPIC)
