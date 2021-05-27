# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KeywordItem(scrapy.Item):

    # 카테고리명(분류1)
    category_first_name = scrapy.Field()

    # 카테고리명(분류2)
    category_second_name = scrapy.Field()

    # 카테고리명(분류3)
    category_third_name = scrapy.Field()
    
    # 순번
    order_num = scrapy.Field()

    # 키워드
    keyword = scrapy.Field()

    # PC 검색수
    search_num_pc = scrapy.Field()

    # 모바일 검색수
    search_num_mobile = scrapy.Field()

    # 검색수 총합
    search_num_total = scrapy.Field()

    # 상품수
    product_num = scrapy.Field()

    # 비율 (상품수 / 검색수 총합)
    rate = scrapy.Field()
