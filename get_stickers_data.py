from bs4 import BeautifulSoup
from requests import get
import json_helpers
import time

data = json_helpers.readJsonData("sticker_links.json")

STICKERS_COLLECTIONS = data["urls"]


def getPageStickers(page):
    bs_page = BeautifulSoup(page.content, "html.parser")
    result_divs = bs_page.find_all("div", class_="result-box")
    stickers = []
    for sticker_div in result_divs:
        a_title = sticker_div.select_one("h3>a")
        if a_title:
            title = a_title.get_text()
            subTitle_h4 = sticker_div.select_one("h4")
            if subTitle_h4:
                subTitle = sticker_div.select_one("h4").get_text()
                name = title + " | " + subTitle
            else:
                name = title
            print(name)
            img_src = sticker_div.select_one("a img")["src"]
            stickers.append({"name": name, "img_src": img_src})
    print("Page collected")
    time.sleep(0.05)
    return stickers


def getStickersData():
    stickers_data = {}
    for sticker_collection in STICKERS_COLLECTIONS:
        page = get(sticker_collection["url"])
        bs = BeautifulSoup(page.content, "html.parser")
        pages_count_ul = bs.find("ul", {"class": "pagination"})
        # have pagination
        if pages_count_ul == None:
            stickers_data[sticker_collection["title"]] = getPageStickers(page)
        else:
            pages_count_ul_children = pages_count_ul.contents
            pages_count = int(pages_count_ul_children[-4].get_text())
            stickers_data[sticker_collection["title"]] = []
            for page_index in range(pages_count):
                url = sticker_collection["url"] + "page=" + str(page_index + 1)
                sticker_page = get(url)
                stickers_data[sticker_collection["title"]].extend(
                    getPageStickers(sticker_page)
                )

        print(
            "Collection ",
            sticker_collection["title"],
            "finished",
        )
    time.sleep(0.10)
    return stickers_data


json_helpers.saveToJsonFile("data", getStickersData(), "stickers_data.json")


# getStickersData()
# getStickersData()
