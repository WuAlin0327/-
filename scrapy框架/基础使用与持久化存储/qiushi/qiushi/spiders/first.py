# -*- coding: utf-8 -*-
import scrapy
from qiushi.items import QiushiItem

class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            # xpath解析到的指定内容被存储到来selector对象
            # extract()该方法可以将selector对象中存储的数据值拿到
            # extract_first()取到第一个数据，等同于extract()[0]
            author = div.xpath('./div/a[2]/h2/text()').extract_first().strip()
            # author = div.xpath('./div/a[2]/h2/text()').extract()[0]
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first().strip()
            # 1. 将解析到的页面数据存储到items对象
            item = QiushiItem()
            item['author'] = author
            item['content'] = content

            # 2.将item对象提交给管道
            yield item

