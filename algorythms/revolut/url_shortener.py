import unittest
from copy import copy
import string
import random

class UrlShortener:
    def __init__(self, shortcut_size = 10):
        self._shortcuts = {} # expanded => shortcut
        self.shortcut_size = shortcut_size

    def shorten(self, url):
        shortcut = self.create_shortcut(url)
        new_shorten_url = None

        parts = url.rsplit('/', 1)
        if len(parts) == 2:
            base_url, _ = parts
            new_shorten_url = base_url + '/' + shortcut
        else:
            new_shorten_url = url
        
        self._shortcuts[url] = new_shorten_url
        return new_shorten_url

    def expand(self, url):
        for expanded_url, shorten_url in self._shortcuts.items():
            if shorten_url == url:
                print('Expanded Url', expanded_url)
                return expanded_url
        return None    

    def get_shorten(self, url):
        return self._shortcuts.get(url)
    
    @property
    def get_size(self):
        return copy(self.size)
    
    @property
    def get_shortcuts(self):
        return copy(self._shortcuts)
    
    def create_shortcut(self, url):
        characters = string.ascii_letters + string.digits
        shortcut = ''.join(random.choice(characters) for _ in range(self.shortcut_size))
        return shortcut

class TestUrlShortener(unittest.TestCase):
    def test_shorten_url(self):
        url_shortener = UrlShortener()
        for _ in range(15):
            long_url = "http://www.revolut.com/".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
            shorten = url_shortener.shorten(long_url)
            self.assertEqual(shorten, url_shortener.get_shorten(long_url))

            print(url_shortener.get_shortcuts)
    def test_expand_url(self):
        url_shortener = UrlShortener()
        long_url = "http://www.revolut.com/fdshfsdjkhfdsjkfhsdjkfdhs"
        shorten = url_shortener.shorten(long_url)
        self.assertEqual(long_url, url_shortener.expand(shorten))

        print(url_shortener.get_shortcuts)

if __name__ == "__main__":
    unittest.main()