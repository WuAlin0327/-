# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# pymysql
# import pymysql
#
# class QiubaiPipeline(object):
#     conn = None
#     cursor = None
#     def open_spider(self,spider):
#         print('爬虫开始')
#         self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='qiubai')
#
#     def process_item(self, item, spider):
#         sql = 'insert into qiubai(author,content) values ("%s","%s")'%(item['author'],item['content'])
#         self.cursor = self.conn.cursor()
#         try:
#             self.cursor.execute(sql)
#             self.conn.commit()
#         except Exception as e:
#             print(e)
#             self.conn.rollback()
#         return item
#
#     def close_spider(self,spider):
#         print('爬虫结束')
#         self.cursor.close()
#         self.conn.close()

################# 使用redis数据库进行数据存储 ##################
import redis

class QiubaiPipeline(object):
    conn = None
    def open_spider(self,spider):
        print('爬虫开始')
        self.conn = redis.Redis(host='127.0.0.1',port=6379)
    def process_item(self, item, spider):
        dic = {
            'author':item['author'],
            'content':item['content']
        }
        # self.conn.lpush('data',dic)
        print('数据写入到redis数据库中')
        return item
    def close_spider(self,spider):
        print('爬虫结束')

class QiubaiFiles(object):

    def process_item(self, item, spider):
        print('数据写入到磁盘文件中')
        return item

class QiubaiMySQL(object):
    def process_item(self, item, spider):
        print('数据写入到mysql数据库中')
        return item
