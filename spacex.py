import requests

from downloader import download_img


def download_img_last_launch(dir_for_img: str):
    response = requests.get("https://api.spacexdata.com/v4/launches/")
    response.raise_for_status()
    all_launches = response.json()
    id_last_launch_with_img = None

    for num, launch in enumerate(all_launches):
        if len(launch["links"]["flickr"]["original"]) > 0:
            id_last_launch_with_img = num

    for spacex_link_img in all_launches[id_last_launch_with_img]["links"]["flickr"]["original"]:
        download_img(spacex_link_img, dir_for_img)
