import time

import requests
from bs4 import BeautifulSoup


def save_to_file(text):
    with open("novel.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n\n")


def get_chapter_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    select_view = soup.find("div", class_="select-view")
    print(select_view)
    if select_view:
        for select_pagination in select_view.find_all(
            "div", class_="select-pagination"
        ):
            select_pagination.decompose()

        save_to_file(select_view.get_text().strip())

    return soup.find("a", class_="next")


if __name__ == "__main__":
    start_url = (
        "https://www.foxaholic.com/novel/jujutsushi-wa-yuusha-narenai/chapter-0-1/"
    )
    current_url = start_url

    while True:
        print(f"Fetching {current_url}")
        next_btn = get_chapter_text(current_url)
        if next_btn:
            current_url = next_btn["href"]
            time.sleep(2)
        else:
            break
