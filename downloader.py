import os
import urllib.parse
from pathlib import Path

import requests


def download_img(url_img: str, save_path: str):
    Path(save_path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url_img)
    response.raise_for_status()
    name_image = "".join(parse_url_img_file(url_img))

    with open(f"{save_path}/{name_image}", 'wb') as file:
        file.write(response.content)


def parse_url_img_file(url: str) -> tuple:
    img_url_path = urllib.parse.urlsplit(url).path
    img_url_path_unquote = urllib.parse.unquote(img_url_path)
    img_file = os.path.split(img_url_path_unquote)[-1]
    img_file_tuple = os.path.splitext(img_file)

    return img_file_tuple
