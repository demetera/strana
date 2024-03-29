import json

import requests
from bs4 import BeautifulSoup

class Strana():
    """Class represents connection to strana.ua"""
    STRANA_URL = 'https://strana.news'
    def __init__(self, day=None, page=1, query=None):
        """Class initialization

        Args:
            day (str, optional): date in format yyyy-mm-dd or `yesterday`. Defaults to None.
            page (int, optional): Page number. Defaults to 1.
        """
        
        if day == None:
            if query != None:
                self.__requrl = '{}/search/page-{}.html?query={}'.format(self.STRANA_URL, page, query)
            else:
                self.__requrl = '{}/news/page-{}.html'.format(self.STRANA_URL, page)
        else:
            self.__requrl = '{}/news/day={}/page-{}.html'.format(self.STRANA_URL, day, page)
        content = requests.get(self.__requrl).text
        self.bs = BeautifulSoup(content, 'html.parser')
        self.__title = self.bs.title.text
        self.__articles = []

    @property
    def get_title(self):
        """Returns title of web page

        Returns:
            str: Title of webpage
        """
        return self.__title

    @property
    def articles(self):
        """Returns list of articles

        Returns:
            list: List of tuples (date, text content, article url)
        """
        return self.__articles

    @property
    def request_url(self):
        """Returns of url compiled when class initialized

        Returns:
            str: Request URL
        """
        return self.__requrl

    def get_articles(self):
        """Appends `__articles` with tuple parameters. See `articles` function
        """
        raw_arts = self.bs.find_all('a', {'class':'article'})
        for art in raw_arts:
            self.__articles.append((art.text.strip(), self.STRANA_URL+art['href']))

    def get_full_articles(self):
        """Appends `__articles` with parameters in tuple. See `articles` function
        """
        raw_arts = self.bs.find_all('article', {'class':'lenta-news clearfix'})
        for art in raw_arts:
            art_date = art.find('time', {'class': 'date'}).text.replace('\n', '')
            art_content = art.find('a', {'class': 'article'}).text.strip()
            art_url = self.STRANA_URL + art.find('a', {'class': 'article'})['href']
            self.__articles.append((art_date, art_content, art_url))


class Article():
    """Class represents article object
    """
    def __init__(self, art_url):
        """Parses article URL and assignes dict object to `__content` value

        Args:
            art_url ([type]): [description]
        """
        conn = requests.get(art_url).text
        parsed = BeautifulSoup(conn, 'html.parser')
        raw_data = parsed.find('script', {'type':'application/ld+json'}).text.strip()
        raw_data = raw_data.replace('\n', '').replace('\r', '')
        raw_data = raw_data.replace('&amp;nbsp;', ' ')
        self.__content = json.loads(raw_data)

    @property
    def content(self):
        """Returns dict object with article content. See initialization

        Returns:
            dict: Dict object with article parameters
        """
        return self.__content
