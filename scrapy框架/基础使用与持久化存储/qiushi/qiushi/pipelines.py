# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiushiPipeline(object):
    file = None
    def open_spider(self,spider):
        # 整个爬虫过程中，该方法只会被调用一次，可以在这里打开文件
        self.file = open('qiubai.txt','w',encoding='utf-8')
        print('开始爬虫')
    def process_item(self, item, spider):
        # 该方法可以接收爬虫文件中提交过来的item对象，并且对item对象中存储页面数据进行持久化存储
        # 参数item表示的就是接收到的item对象
        # 每当爬虫文件向管道提交一次item，则该方法就会被执行一次
        author = item['author']
        content = item['content']
        self.file.write(author+':\n'+content+'\n-------------------\n\n\n')
        return item
    def close_spider(self,spider):
        # 该方法只会在爬虫结束的时候调用一次
        print('爬虫结束')
        self.file.close()


