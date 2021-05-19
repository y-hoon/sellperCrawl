import scrapy


class sellperspider(scrapy.Spider):
    name = 'sellperspider'
    allowed_domains = ['sellper.kr']
    start_urls = ['https://sellper.kr/categories/0']

    def parse(self, response):
        self.logger.info('sellper url ===> {}'.format(response.url))
        self.logger.info('sellper text ====> {}'.format(response.text))



