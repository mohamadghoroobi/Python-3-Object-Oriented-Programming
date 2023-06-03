from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys

LINK_REGEX = re.compile(
    "<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")


class LinkCollector:
    def __init__(self, url):
        self.url = "" + urlparse(url).netloc
        self.collected_links = set()
        self.visited_links = set()

    def collect_links(self, path="/"):
        full_url = self.url + path
        self.visited_links.add(full_url)
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)
        links = {self.normalize_url(path, link) for link in links}
        self.collected_links = links.union(self.collected_links)
        unvisited_links = links.difference(self.visited_links)
        print(links, self.visited_links, self.collect_links, unvisited_links)

    def normalize_url(self, path, link):
        if link.startswith("http://"):
            return link.rstrip("/")
        elif link.startswith("/"):
            return self.url + link.rstrip("/")
        else:
            return (
                self.url
                + path.rpartition("/")[0]
                + "/"
                + link.rstrip("/")
            )


if __name__ == "__main__":
    collector = LinkCollector(sys.argv[1])
    collector.collect_links()
    for link in collector.collected_links:
        print(link)
