from bs4 import BeautifulSoup
from requests import get
import json_helpers


BASE_URL = "https://csgostash.com"
WEAPON_COLLECTIONS_URLS = []


def getWeaponData(weapon):
    url = weapon["href"]
    title = weapon.get_text()
    img_src = weapon.find("img")["src"]
    return {"url": url, "title": title, "img_src": img_src}


def getWeaponsUrls():
    weapons_data = {}
    page = get(BASE_URL)
    bs = BeautifulSoup(page.content, "html.parser")
    pistols = bs.select(".navbar-nav .dropdown:nth-of-type(2) ul li a")
    rifles = bs.select(".navbar-nav .dropdown:nth-of-type(3) ul li a")
    smgs = bs.select(".navbar-nav .dropdown:nth-of-type(4) ul li a")
    heavy = bs.select(".navbar-nav .dropdown:nth-of-type(5) ul li a")

    weapons_data["pistols"] = []
    weapons_data["rifles"] = []
    weapons_data["smgs"] = []
    weapons_data["heavy"] = []

    for weapon in pistols:
        weapons_data["pistols"].append(getWeaponData(weapon))
    for weapon in rifles:
        weapons_data["rifles"].append(getWeaponData(weapon))
    for weapon in smgs:
        weapons_data["smgs"].append(getWeaponData(weapon))
    for weapon in heavy:
        weapons_data["heavy"].append(getWeaponData(weapon))

    return weapons_data


json_helpers.saveToJsonFile("urls", getWeaponsUrls(), "weapon_links.json")
