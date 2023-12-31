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


def process_products(df):
    updated_products = []
    for product in df.to_dict('records'):
        html = get_response(product['url'])
        product['price'] = get_price(html)
        product['alert'] = product['price'] < product["alert_price"]
        updated_products.append(product)
    return pd.DataFrame(updated_products)


def get_response(url):
    response = requests.get(url)
    return response.text


def get_price(html):
    soup = bs4.BeautifulSoup(html, "lxml")
    el = soup.select_one(".price_color")
    price = price_parser.Price.fromstring(el.text)
    return price.amount_float

def main():
    df = get_urls(PRODUCT_URL_CSV)
    df_updated = process_products(df)
    if SAVE_TO_CSV:
        df_updated.to_csv(PRICES_CSV,index=False,mode='a')

main()