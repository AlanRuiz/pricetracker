import smtplib
import pandas as pd
import requests
import bs4
import price_parser

PRODUCT_URL_CSV = "products.csv"
SAVE_TO_CSV = True
PRICES_CSV = "prices.csv"
SEND_MAIL = True


#
def get_urls(csv_file):
    df = pd.read_csv(csv_file)
    return df


# def process_products(df):
#   for product in df.to_dict("records"):
# product["url"] is the URL

def get_response(url):
    response = requests.get(url)
    return response.text


def get_price(html):
    soup = bs4.BeautifulSoup(html, "lxml")
    el = soup.select_one(".price_color")
    price = price_parser.Price.fromstring(el.text)
    return price.amount_float


stuff = get_response("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
print(get_price(stuff))