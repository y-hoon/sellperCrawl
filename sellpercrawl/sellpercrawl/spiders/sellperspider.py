import json
import scrapy


class sellperspider(scrapy.Spider):
    name = 'sellperspider'
    allowed_domains = ['sellper.kr']
    start_urls = ['https://sellper.kr/categories/0']

    def parse(self, response):
        # self.logger.info('sellper url ===> {}'.format(response.url))
        # self.logger.info('sellper text ====> {}'.format(response.text))

        # 첫번째 카테고리 json 값 로딩
        category_one_json = json.loads(response.text).get("childList")

        for ct in category_one_json:
            # print(ct)
            cid = ct.get('cid')
            # print(cid)



            yield scrapy.Request('https://sellper.kr/categories/{}'.format(cid), self.parse_second_category)


    def parse_second_category(self, response):
        # self.logger.info('sellper second category url ===> {}'.format(response.url))
        # self.logger.info('sellper second category text ====> {}'.format(response.text))

        #두번쨰 카테고리 json 값 로딩
        category_two_json = json.loads(response.text).get("childList")

        for ct_two in category_two_json:
            # print(ct_two)
            cid = ct_two.get('cid')
            # print(cid)
            yield scrapy.Request('https://sellper.kr/categories/{}'.format(cid), self.parse_third_category)

    def parse_third_category(self, response):
        # self.logger.info('sellper third category url ===> {}'.format(response.url))
        # self.logger.info('sellper third category text ====> {}'.format(response.text))

        #세번째 카테고리 json 값 로딩
        category_third_json = json.loads(response.text).get("childList")

        for ct_third in category_third_json:
            # print(ct_two)
            cid = ct_third.get('cid')
            # print(cid)



