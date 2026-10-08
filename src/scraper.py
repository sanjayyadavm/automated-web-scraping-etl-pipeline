import requests
from bs4 import BeautifulSoup
from config import BASE_URL, HEADERS

def scrape_quotes():
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        data.append({
            "quote": text,
            "author": author
        })

    return data