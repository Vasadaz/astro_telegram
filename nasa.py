import os
import urllib.parse

import requests
from dotenv import load_dotenv

from downloader import download_img


COUNT_IMG_NASA_APOD = 30
COUNT_IMG_NASA_EPIC = 5
DIR_IMG_NASA_APOD = "images_nasa_apod"
DIR_IMG_NASA_EPIC = "images_nasa_epic"


def download_img_apod(count_img: int, dir_for_img: str):
    nasa_token = os.environ["NASA_TOKEN"]
    payload = {"api_key": nasa_token, "count": count_img}
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    for nasa_day in response.json():
        nasa_link_img = nasa_day.get("hdurl")

        if nasa_link_img:
            download_img(nasa_link_img, dir_for_img)


def download_img_epic(count_img: int, dir_for_img: str):
    nasa_token = os.environ["NASA_TOKEN"]
    payload = {"api_key": nasa_token}
    url = "https://api.nasa.gov/EPIC/api/natural"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    epic_foto_info_list = response.json()

    for number_foto in range(-count_img, 0):
        epic_last_foto_info = epic_foto_info_list[number_foto]
        epic_last_foto_date = epic_last_foto_info["date"][:10].replace("-", "/")
        epic_last_foto_name = epic_last_foto_info["image"]
        epic_last_foto_url = f"https://api.nasa.gov/EPIC/archive/natural/" \
                             f"{epic_last_foto_date}/png/{epic_last_foto_name}.png?"

        download_img(epic_last_foto_url + urllib.parse.urlencode(payload), dir_for_img)


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    download_img_apod(COUNT_IMG_NASA_APOD, DIR_IMG_NASA_APOD)
    download_img_epic(COUNT_IMG_NASA_EPIC, DIR_IMG_NASA_EPIC)
