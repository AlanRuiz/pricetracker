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

