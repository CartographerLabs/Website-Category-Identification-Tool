import requests
from bs4 import BeautifulSoup

class Website:
    '''
    This class is used to create an instance of a website. Having values such as url, titles, and content.

    Note: Somw websites do not allow scraping and so this class will fail to pick up any text on them.
    '''
    website_url = ''
    website_title = ''
    website_content = ''
    main_titles = []
    secondary_titles = []
    tertiary_titles = []
    body_text = []

    def __init__(self, website_url):
        '''
        The constructor
        :param website_url:
        '''

        self.website_title = ''
        self.website_content = ''
        self.main_titles = []
        self.secondary_titles = []
        self.tertiary_titles = []
        self.body_text = []

        self.populate_website(website_url)

    def populate_website(self, url):
        '''
        Used to populate the member variables of this class.
        :param url:
        :return:
        '''
        web_page = requests.get(url)

        self.website_url = web_page.url
        self.website_content = web_page.content
        self._set_body_text(web_page.content)
        self._set_main_titles(web_page.content)
        self._set_secondary_titles(web_page.content)
        self._set_tertiary_titles(web_page.content)


    def _set_main_titles(self, content):
        '''
        Used to set a list of 'h1' titles of this website
        :param content:
        '''
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find_all('h1')
        for result in results:
            self.main_titles.append(result.get_text())

    def _set_secondary_titles(self, content):
        ''' Used to set a list of 'h2' titles of this website
        :param content:
        '''
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find_all('h2')
        for result in results:
            self.secondary_titles.append(result.get_text())


    def _set_tertiary_titles(self, content):
        ''' Used to set a list of 'h3' titles of this website
        :param content:
        '''
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find_all('h3')
        for result in results:
            self.tertiary_titles.append(result.get_text())

    def _set_body_text(self, content):
        '''
        Used to set all of the 'p' text in this website.
        :param content:
        '''
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find_all('p')
        for result in results:
            self.body_text.append(result.get_text())