import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from djadminka.models import Vacanci_2
from django.core.management.base import BaseCommand

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
LINK = "https://freelance.habr.com/tasks?page=1&q=python"
names = []
chrome_options = Options()
chrome_options.add_argument("--headless")
reg = re.compile('[^a-zA-Z 0-9а-яёА-ЯЁ]')


def sum_list(list):
    F = ''
    for g in list:
        F += g
    return F


def number_of_pages(soup):
    if soup.find('div', class_="pagination"):
        divi = soup.find('div', class_="pagination").find_all('a')
        return int(divi[-2].get_text())
    else:
        return 1


def ifi_2(N):
    if N:
        return N.find('i', class_='params__count').get_text()
    else:
        return 'Не указан'


def get_html(link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    html = driver.page_source
    return html


def get_price(link):
    Html = get_html(link)
    soup = BeautifulSoup(Html, "html.parser")
    return reg.sub('', soup.find('div', class_='task__finance').get_text())


def divi_parse(divi):
    for t in divi:
        N = 'https://freelance.habr.com' + t.find('div', class_='task__title').find('a').get('href')
        names.append({
            'Title': t.find('div', class_='task__title').get_text(),
            'Link': N,
            'Price': get_price(N),
            "Number_of_otkliks": ifi_2(t.find('span', class_='params__responses icon_task_responses')),
            'Number_of_vues': ifi_2(t.find('span', class_="params__views icon_task_views"))
        })


def parse():
    Html = get_html(LINK)
    soup = BeautifulSoup(Html, "html.parser")
    divi = soup.find_all('li', class_='content-list__item')
    divi_parse(divi)
    Ni = number_of_pages(soup)
    if Ni > 1:
        for i in range(2, Ni + 1):
            LINK_2 = LINK + f'&page={i}'
            Html = get_html(LINK_2)
            soup = BeautifulSoup(Html, "html.parser")
            divi = soup.find_all('li', class_='content-list__item')
            divi_parse(divi)


class Command(BaseCommand):
    help = "Парсер номер 2"

    def handle(self, *args, **options):
        parse()
