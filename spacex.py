import requests

from downloader import download_img


DIR_IMG_SPACEX = "images_spacex"


def download_last_launch_imgs(save_dir: str):
    response = requests.get("https://api.spacexdata.com/v4/launches/")
    response.raise_for_status()
    launches = response.json()

    for launch in launches[::-1]:
        img_urls = launch["links"]["flickr"]["original"]

        if img_urls:
            for url in img_urls:
                download_img(url, save_dir)
            break


if __name__ == "__main__":
    download_last_launch_imgs(DIR_IMG_SPACEX)
