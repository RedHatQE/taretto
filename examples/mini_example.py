#!env python
"""
  Sentaku pypi search exampple
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  before running::

    $ pip install selenium  requests sentaku
"""
import argparse
import contextlib
import sentaku
import requests
import attr
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

parser = argparse.ArgumentParser()
parser.add_argument('query')
parser.add_argument('--fast', action='store_true')


@attr.s
class FastSearch(object):
    get = staticmethod(requests.get)


@attr.s
class Browser(object):
    driver = attr.ib()

    def __getattr__(self, key):
        return getattr(self.driver, key)


class SearchContext(sentaku.ImplementationContext):
    pass


@attr.s
class Search(sentaku.Element):
    """sentaku element for really simple pypi searching"""
    base_url = attr.ib(default='https://pypi.python.org/pypi')

    search = sentaku.ContextualMethod()
    open_page = sentaku.ContextualMethod()


@SearchContext.external_for(Search.search, Browser)
def search_browser(self, text):
    """do a slow search via the website and return the first match"""
    self.impl.get(self.base_url)

    search_div = self.impl.find_element_by_id('search')
    search_term = search_div.find_element_by_id('term')
    search_term.send_keys(text)
    search_div.find_element_by_id('submit').click()
    e = self.impl.find_element_by_css_selector('table.list tr td a')
    return e.get_attribute('href')


@SearchContext.external_for(Search.search, FastSearch)
def search_fast(self, text):
    """do a sloppy quick "search" via the json index"""

    resp = self.impl.get(
        '{base_url}/{text}/json'.format(base_url=self.base_url, text=text))
    return resp.json()['info']['package_url']


@SearchContext.external_for(Search.open_page, Browser)
def open_page(self, url):
    self.impl.get(url)


def main(search, query):
    """main function that does the search"""
    url = search.search(query)
    print(url)
    search.open_page(url)


def cli_main():
    """cli entrypoitns, sets up everything needed"""
    SearchContext.commit()
    args = parser.parse_args()
    # open up a browser
    firefox_remote = Remote(
        'http://127.0.0.1:4444/wd/hub',
        DesiredCapabilities.FIREFOX)
    with contextlib.closing(firefox_remote):
        context = SearchContext.from_instances([FastSearch(), Browser(firefox_remote)])
        search = Search(parent=context)

        if args.fast:
            with context.use(FastSearch, Browser):
                main(search, args.query)
        else:
            with context.use(Browser):
                main(search, args.query)


if __name__ == '__main__':
    cli_main()
