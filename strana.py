from bs4 import BeautifulSoup
import requests
import json


class Strana():
    STRANA_URL = 'https://strana.ua'
    def __init__(self, day=None, page=1):
        if day == None:
            self.__requrl = '{}/news/page-{}.html'.format(self.STRANA_URL, page)
        else:
            self.__requrl = '{}/news/day={}/page-{}.html'.format(self.STRANA_URL, day, page)
        content = requests.get(self.__requrl).text
        self.bs = BeautifulSoup(content, 'html.parser')
        self.__title = self.bs.title.text
        self.__articles = []

    @property
    def get_title(self):
        return self.__title

    @property
    def articles(self):
        return self.__articles

    @property
    def request_url(self):
        return self.__requrl

    def get_articles(self):
        raw_arts = self.bs.find_all('a', {'class':'article'})
        for art in raw_arts:
            self.__articles.append((art.text.strip(), self.STRANA_URL+art['href']))

    def get_full_articles(self):
        raw_arts = self.bs.find_all('article', {'class':'lenta-news clearfix'})
        for art in raw_arts:
            art_date = art.find('time', {'class': 'date'}).text.replace('\n', '')
            art_content = art.find('a', {'class': 'article'}).text.strip()
            art_url = self.STRANA_URL + art.find('a', {'class': 'article'})['href']
            self.__articles.append((art_date, art_content, art_url))


class Article():
    def __init__(self, art_url):
        conn = requests.get(art_url).text
        parsed = BeautifulSoup(conn, 'html.parser')
        raw_data = parsed.find('script', {'type':'application/ld+json'}).text.strip()
        raw_data = raw_data.replace('\n', '').replace('\r', '')
        raw_data = raw_data.replace('&amp;nbsp;', ' ')
        self.__content = json.loads(raw_data)

    @property
    def content(self):
        return self.__content
