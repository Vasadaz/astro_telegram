import os
import urllib.parse
from pathlib import Path

import requests
from dotenv import load_dotenv


def download_img(url_img: str, save_path: str):
    Path(save_path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url_img)
    response.raise_for_status()
    name_image = "".join(parser_img_file(url_img))

    with open(f"{save_path}/{name_image}", 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(id_launch: int):
    response = requests.get("https://api.spacexdata.com/v4/launches/")
    response.raise_for_status()

    for spacex_link_img in response.json()[id_launch]["links"]["flickr"]["original"]:
        download_img(spacex_link_img, "images_spacex")


def parser_img_file(url: str) -> tuple:
    img_url_path = urllib.parse.urlsplit(url).path
    img_url_path_unquote = urllib.parse.unquote(img_url_path)
    img_file = os.path.split(img_url_path_unquote)[-1]
    img_file_tuple = os.path.splitext(img_file)

    return img_file_tuple


def nasa_apod_img(count_img: int):
    nasa_token = os.environ["NASA_TOKEN"]
    payload = {"api_key": nasa_token, "count": count_img}
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params=payload)
    response.raise_for_status()

    for nasa_day in response.json():
        nasa_link_img = nasa_day.get("hdurl")

        if nasa_link_img is not None:
            download_img(nasa_link_img, "images_nasa_apod")


def nasa_epic_img(count_img: int):
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

        download_img(epic_last_foto_url + urllib.parse.urlencode(payload), "images_nasa_epic")


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    fetch_spacex_last_launch(156)
    nasa_apod_img(30)
    nasa_epic_img(5)
