from pathlib import Path

import requests


def download_img(url_img: str, save_path: str):
    Path(save_path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url_img)
    response.raise_for_status()
    name_image = url_img.split("/")[-1]
    with open(f"{save_path}/{name_image}", 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(id_launch: int):
    response = requests.get("https://api.spacexdata.com/v4/launches/")
    response.raise_for_status()

    for spacex_link_img in response.json()[id_launch]["links"]["flickr"]["original"]:
        download_img(spacex_link_img, "images")


if __name__ == "__main__":
    fetch_spacex_last_launch(156)
