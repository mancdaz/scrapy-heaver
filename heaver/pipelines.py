# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

host = 'localhost'
user = 'snickers'
password = 'snickers'
port = 3306
db = 'websites'

class HeaverPipeline(object):
    def process_item(self, item, spider):
        return item

class HeaverMysqlPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        guid = self._get_guid((item)
        try:
            self.cursor.execute("""INSERT INTO snickers (
            guid,
            item_num,
            item_name,
            item_colour_num,
            item_colour_desc,
            item_link,
            item_desc'
            item_features'
            item_sizes'
            item_addl_info'
            image_urls') VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """,
            guid,
            item['item_num'],
            item['item_name'],
            item['item_colour_num'],
            item['item_colour_desc'],
            item['item_link'],
            item['item_desc'],
            item['item_features'],
            item['item_sizes'],
            item['item_addl_info',
            item['image_urls'])



    def _get_guid(self, item):
        """ Generate a unique identifier based on product code and product colour """
        return '%s-%s' % (item['item_num'], item['item_colour_num'])




