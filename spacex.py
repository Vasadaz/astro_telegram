import requests

from downloader import download_img


def download_img_last_launch(dir_for_img: str):
    response = requests.get("https://api.spacexdata.com/v4/launches/")
    response.raise_for_status()
    all_launches = response.json()

    for launch in all_launches[::-1]:
        launch_img_links = launch["links"]["flickr"]["original"]

        if len(launch_img_links) > 0:
            for link in launch_img_links:
                download_img(link, dir_for_img)

            break
