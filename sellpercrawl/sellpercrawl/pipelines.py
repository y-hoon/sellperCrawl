# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import xlsxwriter


class SellperSpiderPipeline:

    # 초기화 메소드
    def __init__(self):
        self.workbook = xlsxwriter.Workbook('D:/crawling/sellper_keyword.xlsx')
        self.worksheet = self.workbook.add_worksheet('키워드목록')
        self.count = 2

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('==== Write Header ====')

        self.worksheet.write('A1', '카테고리명(분류1)')
        self.worksheet.write('B1', '카테고리명(분류2)')
        self.worksheet.write('C1', '카테고리명(분류3)')
        self.worksheet.write('D1', '순번')
        self.worksheet.write('E1', '키워드')
        self.worksheet.write('F1', 'PC 검색수')
        self.worksheet.write('G1', '모바일 검색수')
        self.worksheet.write('H1', '검색수 총합')
        self.worksheet.write('I1', '상품수')
        self.worksheet.write('J1', '비율 (상품수 / 검색수 총합)')

    # Item 건별 실행
    def process_item(self, item, spider):
        self.worksheet.write('A%s' % self.count, item.get('category_first_name'))
        self.worksheet.write('B%s' % self.count, item.get('category_second_name'))
        self.worksheet.write('C%s' % self.count, item.get('category_third_name'))
        self.worksheet.write('D%s' % self.count, item.get('order_num'))
        self.worksheet.write('E%s' % self.count, item.get('keyword'))
        self.worksheet.write('F%s' % self.count, item.get('search_num_pc'))
        self.worksheet.write('G%s' % self.count, item.get('search_num_mobile'))
        self.worksheet.write('H%s' % self.count, item.get('search_num_total'))
        self.worksheet.write('I%s' % self.count, item.get('product_num'))
        self.worksheet.write('J%s' % self.count, item.get('rate'))

        self.count += 1

        return item

    def close_spider(self, spider):
        spider.logger.info('==== Excel Write End ====')

        self.workbook.close()
