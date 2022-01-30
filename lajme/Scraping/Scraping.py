from pprint import pprint
import re
from bs4 import BeautifulSoup
import requests
from summary.algorithms.scoring import scoring_algorithm


def cnn_scraping():
    page = requests.get("http://rss.cnn.com/rss/edition.rss")
    soup = BeautifulSoup(page.content, features="xml")
    items = soup.find_all('item')
    newsDict = dict()
    titles = []
    links = []
    for i in items[:5]:
        titles.append(i.title.get_text())
        links.append(i.link.get_text())

    for count, l in enumerate(links):
        page1 = requests.get(l)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        pg = ''
        if re.match(r'^https://money.cnn', l) is not None:
            body_div_m = soup1.find('div', class_='storytext')
            body_p = body_div_m.find_all('p')
            for p in body_p:
                pg = pg + '\n' + p.get_text()
        else:
            body_div = soup1.find_all('div', class_='zn-body__paragraph')
            for div in body_div:
                pg = pg + '\n' + div.get_text()
        result_list = scoring_algorithm.scoring_main(pg, 5)
        summary = ' '.join(result_list)
        newsDict[titles[count]] = summary
    return newsDict