import os
import urllib.parse
from pathlib import Path

import requests


def download_img(url_img: str, save_path: str):
    Path(save_path).mkdir(parents=True, exist_ok=True)
    name_img = search_full_name_image(url_img)

    response = requests.get(url_img)
    response.raise_for_status()

    with open(f"{save_path}/{name_img}", 'wb') as file:
        file.write(response.content)


def search_full_name_image(url: str) -> str:
    img_url_path = urllib.parse.urlsplit(url).path
    img_url_path_unquote = urllib.parse.unquote(img_url_path)
    img_file = os.path.split(img_url_path_unquote)[-1]
    img_file_tuple = os.path.splitext(img_file)
    name_img = "".join(img_file_tuple)

    return name_img
