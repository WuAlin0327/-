# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.qiushibaike.com/text/']
    start_urls = ['https://www.qiushibaike.com/text/']
    pageNum = 1
    url = 'https://www.qiushibaike.com/text/page/%d/'
    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()
            item = QiubaiItem()
            item['author'] = author
            item['content'] = content
            yield item
        print('还在执行吗')
        # 使用手动请求方式进行多个url爬取
        if self.pageNum <= 13:
            self.pageNum += 1
            print('执行了码', self.pageNum)
            # 判断页码是否小于13
            new_url = format(self.url % self.pageNum)
            # callback函数是回调函数，第二页解析的内容与开始解析的内容是一样的，可以使用parse函数进行解析，也可以自己定义函数进行解析
            yield scrapy.Request(url=new_url,callback=self.parse)
