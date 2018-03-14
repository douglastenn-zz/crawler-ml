import fire
from crawler_ml.crawler_handler import CrawlerHandler


class Crawler(object):
    """A task runner class."""

    def start(self):
        """
        Start crawler
        """
        return CrawlerHandler().handler()


if __name__ == '__main__':
    fire.Fire(Crawler)
