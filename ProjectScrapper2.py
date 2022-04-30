import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
time.sleep(3)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find_all("table", attrs={"class": ["wikitable", "sortable", "jquery-tablesorter"]})[1]

def scrape():
    headers = ["star", "constellation", "right_ascension", "declination", "apparent_magnitude", "distance", "spectral_type", "mass", "radius", "discovery_year"]
    star_data = []

    for row in table.find_all("tr"):
        cols = row.find_all("td")

        if len(cols) == 0:
            continue

        temp = []

        for col in cols:
            data = col.text.strip()

            str_encode = data.encode("ascii", "ignore")
            str_decode = str_encode.decode()

            temp.append(str_decode)

        star_data.append(temp)

    with open("stars.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for row in star_data:
            writer.writerow(row)

scrape()