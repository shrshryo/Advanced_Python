from bs4 import BeautifulSoup
import requests
import json
data = []
start_url = 'https://www.osta.ee/en/category/computers/desktop-computers'
page = requests.get(start_url)
soup = BeautifulSoup(page.text, 'html.parser')

def parse(start_url):
    page = requests.get(start_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    objects = soup.find_all("figure", class_="offer-thumb")

    for object in objects:
        item = {}
        item["Title"] = object.find("div", {"class": "offer-thumb__content"}).find("h3")["title"]
        if object.find("div", {"class": "offer-thumb__price--current"}) != None:
            scarp = object.find("div", {"class": "offer-thumb__price--current"}).find("span")
            if scarp != None:
                scarp.extract()
            item["Price"] = object.find("div", {"class": "offer-thumb__price--current"}).text.strip().replace('\n', "")
        else:
            continue
        item["Picture href"] = object.find("figure", {"class": "offer-thumb__image"}).find("a")["data-original"]
        data.append(str(item))

    next_page_url = soup.find("a", class_="next")['href']
    next_page = "https://www.osta.ee/en/" + next_page_url

    try:
        parse(next_page)
    except KeyError:
        print("no more page")

parse(start_url)
data = list(data)
data_json = json.dumps(data, ensure_ascii=False, indent=4)

f = open("output.json", "w", encoding='utf-8')
f.write(data_json)
f.close()