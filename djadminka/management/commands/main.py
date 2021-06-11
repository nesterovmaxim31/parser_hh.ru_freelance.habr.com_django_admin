import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from djadminka.models import Vacanci
from django.core.management.base import BaseCommand

Chablon = re.compile("[0-9 А-ЯA-Za-zа-я.:–]")
Chablon_2 = re.compile(r"https://hh[.]{1}ru/vacancy/[\d]*")
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
LINK = "https://hh.ru/search/vacancy?st=searchVacancy&L_profession_id=1.1&area=1646&no_magic=true&text=Системный+администратор"
names = []
chrome_options = Options()
chrome_options.add_argument("--headless")


def sum_list(list):
    F = ''
    for g in list:
        F += g
    return F


def number_of_page(soup):
    divi = soup.find('span', class_="bloko-button-group")
    return int(divi.get_text()[-1])


def ifi(N):
    if N:
        return True
    else:
        return False


def ifi_2(N):
    if N:
        return sum_list(Chablon.findall(N.get_text()))
    else:
        return "Не указан"


def get_html_2(link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    html = driver.page_source
    return html


def divi_parse(divi):
    for t in divi:
        if t.find('a', class_="vacancy-serp-item__special"):
            continue
        D = {
            'Title': t.find('a', class_="bloko-link").get_text(),
            'Link': sum_list(Chablon_2.findall(t.find('a', class_="bloko-link").get('href'))),
            'Salary': sum_list(Chablon.findall(t.find("div", class_="vacancy-serp-item__sidebar").get_text())),
            'No-resume': ifi(t.find("div", class_="vacancy-label vacancy-label_no-resume")),
            'First': ifi(t.find("div", {'data-qa': "vacancy-label-be-first"})),
            'Company': ifi_2(t.find('a', class_="bloko-link bloko-link_secondary")),
            'Date': t.find('span',
                           class_="vacancy-serp-item__publication-date vacancy-serp-item__publication-date_short").get_text(),
            "Address": ifi_2(t.find("span", class_="vacancy-serp-item__meta-info"))}
        Vacanci(Title=D['Title'], Link=D['Link'], Salary=D['Salary'], No_resume=D['No-resume'], First=D['First'],
                Company=D['Company'], Date=D['Date']).save()


def parse():
    Html = get_html_2(LINK)
    soup = BeautifulSoup(Html, "html.parser")
    Ni = number_of_page(soup)
    divi2 = soup.find_all("div", class_="vacancy-serp-item")
    divi_parse(divi2)
    for i in range(1, Ni):
        LINK_2 = LINK.replace("page=0", f'page={i}')
        Html = get_html_2(LINK_2)
        soup = BeautifulSoup(Html, "html.parser")
        divi2 = soup.find_all("div", class_="vacancy-serp-item")
        divi_parse(divi2)


#   return f"{D['Title']}\t{D['Link']}\t{D['Salary']}\t{D['No-resume']}\t{D['First']}\t{D['Company']}\t{D['Date']}"


class Command(BaseCommand):
    help = "Парсер"

    def handle(self, *args, **options):
        parse()
