import BeautifulSoup
from soupselect import select

class BeautifulSoupSelect(object):
    """
    >>> html = '<html><body><div id="foo">bar</div></body></html>'
    >>> bss = BeautifulSoupSelect(html)
    >>> bss('#foo')[0].text
    u'bar'
    """    
    
    def __init__(self, html):
        super(BeautifulSoupSelect, self).__init__()
        self.bs = BeautifulSoup.BeautifulSoup(html)

    def __call__(self, selector):
        return select(self.bs, selector)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
        