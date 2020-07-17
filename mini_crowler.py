import re
import urllib.request


class Website:
    def __init__(self, url):
        self.url = url
        self.__text = None
        self.__emails = None
        self.__links = None

    @property
    def text(self):
        if self.__text is None:
            with urllib.request.urlopen(self.url) as req:
                self.__text = req.read().decode('utf-8')
        return self.__text

    @property
    def emails(self):
        if self.__emails is None:
            pattern = r"[a-z]+@[a-z]+.[a-z]"
            self.__emails = findall(pattern, self.text)
        return self.__emails

    @property
    def links(self):
        if self.links is None:
            pattern = r'<[^>]*href="(^"]*)"'
            self.__links = re.findall(pattern, self.text)
            return self.__links


url = "www.python.com"
website = Website(url)
print(websit.text)
print(website.emails)
# type(website.links)
