from pathlib import Path

import requests


def download_img(url_img: str, save_path: str):
    Path(save_path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url_img)
    response.raise_for_status()

    with open(f"{save_path}/name_img.jpg", 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    download_img("https://drasler.ru/wp-content/uploads/2019/05/%D0%9A%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D1%81-%D1%85%D0%BE%D1%80%D0%BE%D1%88%D0%B8%D0%BC-%D0%BA%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%D0%BC-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9-%D1%81%D1%82%D0%BE%D0%BB-%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1%80%D0%BA%D0%B0-22.jpg",
                 "images")
