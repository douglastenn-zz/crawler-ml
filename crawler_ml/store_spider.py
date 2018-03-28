import scrapy


class StoreSpider(scrapy.Spider):
    """Class to get all store basic info"""

    name = 'mlspidey'
    start_urls = ['https://www.mercadolivre.com.br/lojas-oficiais']

    def parse(self, response):
        for brand_line in response.css('.brands-list.mesh-row'):
            yield brand_line.css('.brand-wrapper a').extract_first()
