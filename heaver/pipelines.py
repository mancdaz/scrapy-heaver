# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from datetime import datetime

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
        ''' insert or update if exists '''
        guid = self._get_guid(item)
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')

        self.cursor.execute("""SELECT EXISTS(
            SELECT 1 from snickers where guid = \"%s\"
            )""" % guid)
        exists = self.cursor.fetchone()[0]

        if exists:
            sql = "UPDATE snickers \
                  set item_num=\"%s\", \
                  item_name=\"%s\", \
                  item_colour_num=\"%s\", \
                  item_colour_desc=\"%s\", \
                  item_link=\"%s\", \
                  item_desc=\"%s\", \
                  item_features=\"%s\", \
                  item_sizes=\"%s\", \
                  item_addl_info=\"%s\", \
                  image_urls=\"%s\", \
                  updated=\"%s\" \
                  WHERE guid=\"%s\"" % (
                     item['item_num'],
                     item['item_name'],
                     item['item_colour_num'],
                     item['item_colour_desc'],
                     item['item_link'],
                     item['item_desc'],
                     item['item_features'],
                     item['item_sizes'],
                     item['item_addl_info'],
                     item['image_urls'],
                     now,
                     guid,)
        else:
            sql = "INSERT INTO snickers(guid, \
                  item_num, \
                  item_name, \
                  item_colour_num, \
                  item_colour_desc, \
                  item_link, \
                  item_desc, \
                  item_features, \
                  item_sizes, \
                  item_addl_info, \
                  image_urls, \
                  updated) \
                  VALUES (\"%s\", \"%s\", \"%s\", \
                  \"%s\", \"%s\", \"%s\", \
                  \"%s\", \"%s\", \"%s\", \
                  \"%s\", \"%s\", \"%s\")" \
                  % (guid,
                     item['item_num'],
                     item['item_name'],
                     item['item_colour_num'],
                     item['item_colour_desc'],
                     item['item_link'],
                     item['item_desc'],
                     item['item_features'],
                     item['item_sizes'],
                     item['item_addl_info'],
                     item['image_urls'],
                     now)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            self.conn.rollback()

    def _get_guid(self, item):
        """ Generate a unique identifier """
        return '%s-%s' % (item['item_num'], item['item_colour_num'])
