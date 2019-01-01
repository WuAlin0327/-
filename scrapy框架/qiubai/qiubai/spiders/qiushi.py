# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['http://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            author = div.xpath('./div/a[2]/h2/text()').extract_first().strip()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first().strip()
            item = QiubaiItem()
            item['author'] = author
            item['content'] = content
            yield item