import requests

from downloader import download_img


def douwnload_img_last_launch(id_launch: int, dir_for_img: str):
    response = requests.get("https://api.spacexdata.com/v4/launches/")
    response.raise_for_status()

    for spacex_link_img in response.json()[id_launch]["links"]["flickr"]["original"]:
        download_img(spacex_link_img, dir_for_img)
