from bs4 import BeautifulSoup
import requests


URL = "https://pizza.od.ua"

CLASSES = {
    "text": "catalog-item-text",
    "price": "catalog-not-hidden -cheese",
    "img": "catalog-item-img",
    "name": "catalog-name",
    "catalog": "catalog-list",
    "price_lvl1": "bx_catalog_item_price catalog-price",
    "price_lvl2": "bx_price price"
}

CATALOG_ID = "products_content"

ELEMENT_TAG_NAME = "div"

STR_CLASS = "class"
STR_ID = "id"
STR_NAME = "name"
STR_PRICE = "price"
STR_IMG_URL = "image_url"
STR_TEXT = "text"
REALSRC = "data-realsrc"

content = requests.get(URL).text
parser = BeautifulSoup(content, "lxml")
catalog = parser.find(ELEMENT_TAG_NAME, attrs={STR_CLASS: CLASSES["catalog"], STR_ID: CATALOG_ID})

names = list()
prices = list()
texts = list()
images = list()
results = list()

def find_all_from_catalog(attrs={}):
    return catalog.find_all(ELEMENT_TAG_NAME, attrs=attrs)

for div in find_all_from_catalog({STR_CLASS: CLASSES["name"]}):
    names.append(div.a.text)

for div in find_all_from_catalog({STR_CLASS: CLASSES["price"]}):
    str_price = (div.form
        .find(ELEMENT_TAG_NAME, attrs={STR_CLASS: CLASSES["price_lvl1"]})
        .find(ELEMENT_TAG_NAME, attrs={STR_CLASS: CLASSES["price_lvl2"]})
        .text)

    prices.append(int(str_price[0:len(str_price) - 2:1]))

for div in find_all_from_catalog({STR_CLASS: CLASSES["text"]}):
    texts.append(div.p.text)

for div in find_all_from_catalog({STR_CLASS: CLASSES["img"]}):
    images.append(URL + div.img[REALSRC])

for i in range(len(names)):results.append({
        STR_NAME: names[i],
        STR_PRICE: prices[i],
        STR_TEXT: texts[i],
        STR_IMG_URL: images[i]
    })

print(results)
