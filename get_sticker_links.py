from bs4 import BeautifulSoup
from requests import get
import json

BASE_URL = "https://csgostash.com"

STICKER_COLLECTIONS_URLS = []


def getStickerUrls():
    page = get(BASE_URL)
    bs = BeautifulSoup(page.content, "html.parser")
    bs_stickers_a = bs.select(".navbar-nav .dropdown:nth-of-type(9) ul li a")
    # print(bs_stickers_a)
    for tournament in bs_stickers_a:
        href = tournament.get("href")
        title = tournament.get_text()

        STICKER_COLLECTIONS_URLS.append({"url": href, "title": title})


# getStickerUrls()
# json_obj = json.dumps({"urls": STICKER_COLLECTIONS_URLS})
# with open("sticker_links.json", "w") as outfile:
#     outfile.write(json_obj)
