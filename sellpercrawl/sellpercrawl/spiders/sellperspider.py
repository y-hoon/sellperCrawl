import json
import scrapy

from ..items import KeywordItem


class SellperSpider(scrapy.Spider):
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
            category_first_name = ct.get('name')
            # print(cid)

            # 키워드 조회
            yield scrapy.Request('https://sellper.kr/stats/{}'.format(cid), self.parse_keyword, meta={'category_first_name': category_first_name})

            # yield scrapy.Request('https://sellper.kr/categories/{}'.format(cid), self.parse_second_category)


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


    # 키워드 처리
    def parse_keyword(self, response):
        # self.logger.info('sellper category keyword url ===> {}'.format(response.url))
        # self.logger.info('sellper category keyword text ====> {}'.format(response.text))

        keywords = json.loads(response.text).get("data")

        for keyword in keywords:
            # print(keyword)
            # print()

            item = KeywordItem()
            item['category_first_name'] = response.meta['category_first_name']

            try:
                item['category_second_name'] = response.meta['category_second_name']
            except KeyError:
                item['category_second_name'] = ''

            try:
                item['category_third_name'] = response.meta['category_third_name']
            except KeyError:
                item['category_third_name'] = ''

            item['order_num'] = keyword.get('rank')
            item['keyword'] = keyword.get('keyword')
            item['search_num_pc'] = keyword.get('mpcqry')
            item['search_num_mobile'] = keyword.get('mmoqry')
            item['search_num_total'] = int(keyword.get('mmoqry')) + int(keyword.get('mpcqry'))
            item['product_num'] = keyword.get('item_num')
            item['rate'] = round(int(keyword.get('item_num')) / int(item['search_num_total']), 4)

            # print(dict(item))

            yield item
