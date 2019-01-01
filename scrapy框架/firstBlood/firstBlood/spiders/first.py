 # -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称: 通过爬虫文件名称可以指定定位到某一个具体的爬虫文件
    name = 'first'

    # 允许的域名：只可以爬取指定域名下的页面数据
    allowed_domains = ['https://www.qiushibaike.com']
    # 起始url：当前工程将要爬取页面所对应的url
    start_urls = ['http://www.qiushibaike.com/']

    # 解析方法：对获取的页面数据进行指定内容的解析
    # response:根据起始url列表发起请求，请求成功后返回的响应对象
    # parse方法的返回值：必须为迭代器或者空
    def parse(self, response):
        print(response.text)
        print('执行结束')
