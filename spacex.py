import requests

from downloader import download_img


DIR_IMG_SPACEX = "images_spacex"


def download_img_last_launch(dir_for_img: str):
    response = requests.get("https://api.spacexdata.com/v4/launches/")
    response.raise_for_status()
    all_launches = response.json()

    for launch in all_launches[::-1]:
        launch_img_links = launch["links"]["flickr"]["original"]

        if launch_img_links:
            for link in launch_img_links:
                download_img(link, dir_for_img)

            break


if __name__ == "__main__":
    download_img_last_launch(DIR_IMG_SPACEX)
