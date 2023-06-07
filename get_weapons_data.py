from bs4 import BeautifulSoup
from requests import get
import json_helpers
import time


def getPageWeapons(page):
    bs_page = BeautifulSoup(page.content, "html.parser")
    result_divs = bs_page.find_all("div", class_="result-box")
    weapons = []
    for weapon_div in result_divs:
        a_title = weapon_div.select_one("h3>a")
        if a_title:
            title = a_title.get_text()
            img_src = weapon_div.select_one("a img")["src"]
            weapons.append({"name": title, "img_src": img_src})
    time.sleep(0.1)
    return weapons


def getWeaponsData(links_data):
    weapons_data = {}
    for weapon_category in links_data:
        weapons_data[weapon_category] = {}
        for weapon_link in links_data[weapon_category]:
            page = get(weapon_link["url"])
            page_weapons = getPageWeapons(page)
            weapons_data[weapon_category][weapon_link["title"]] = {
                "img_src": weapon_link["img_src"],
                "data": page_weapons,
            }

            print(weapon_link["title"] + "collected")
    return weapons_data


links_data = json_helpers.readJsonData("weapon_links.json")
weapons_data = getWeaponsData(links_data["urls"])
json_helpers.saveToJsonFile("data", weapons_data, "weapons_data.json")
