import html.parser


class _LinksParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return

        for name, value in attrs:
            if name != 'href':
                continue

            self.links.append(value)

class Links:
    def __init__(self, html):
        parser = _LinksParser()
        parser.feed(html)
        links = []
        for link in parser.links:
            if link in links:
                continue
            links.append(link)
        self._links = links

    def all(self):
        return self._links
