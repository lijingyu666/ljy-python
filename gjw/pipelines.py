# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class GjwPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', password='123456', port=3306, db='pro',
                                    charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        print('----')
        print(item['name'])
        try:
            sql = 'INSERT INTO jianli_3(name,sex,stu,work,age,address,salary,towork) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (
                item['name'], item['sex'], item['stu'], item['work'], item['age'], item['address'], item['salary'],
                item['towork']))
            self.conn.commit()
            print('chengogngdb')
            return item
        except:
            print('shibaidb')
            return item

