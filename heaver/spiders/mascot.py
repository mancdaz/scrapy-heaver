#!/usr/bin/env python

import scrapy
import re

cols = {}

class MascotSpider(scrapy.Spider):
    name = "mascot"

    start_urls = [
       # 'https://www.mascotworkwear.co.uk/en/assortment#ss=*&mpt=&pt=&sb=&f=&mf=&mc=&pr=&q=&ce=&mce=&si=&mis=&hc=&p=&at=Clothes',
        'https://www.mascotworkwear.co.uk/en/assortment#ss=*&mpt=%7B892E15E0-65EB-40DE-9430-2F01F4DCDB84%7D%2C%7BAA036A74-EAD3-4A1A-895B-6033AC8B6D6C%7D%2C%7B81FB9C8D-DD0A-4D5D-9893-FB527BAC65FB%7D%2C%7BDBBB862D-7BA1-4E45-B6C6-EFF7FF6E92A0%7D%2C%7B0B16B7BC-DDEF-4DA0-A803-5B1F807DB79A%7D%2C%7BF73C930E-5DE4-45DC-A0F6-885DF27EADAD%7D%2C%7B98829AD3-0C97-43AF-98AF-0574F9878E7A%7D%2C%7B99A52E26-E44A-4E15-BC84-DAA83F1FECB2%7D%2C%7B1395F57B-F226-4D4B-B713-D4525B74276C%7D%2C%7B5DB54D02-4D51-4E03-9489-DD286A534747%7D%2C%7B80A2F872-3313-43D6-9B72-9F0F36720962%7D%2C%7BDAC31118-1DE6-42DB-B8EB-0AC13AF03F48%7D%2C%7B996B643E-B3DC-47EA-BDEF-014FF7D96A36%7D%2C%7B6216435F-5B5D-4507-B6D6-A2BE8A7E03E4%7D%2C%7BF9E7CB81-6F6D-40D1-A7F9-E0263910D9D1%7D&pt=&sb=&f=&mf=&mc=&pr=&q=&ce=&mce=&si=&mis=&hc=&p=&at=Clothes'

    ]

    custom_settings = {
            'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 100,
#                               'heaver.pipelines.HeaverMysqlPipeline': 200,
        }
    }


    def parse(self, response):

        global cols

        # get all colors and convert to names and pop in a dict for lookup
        # later
#        colours = list(set(response.css('.colors a img::attr(src)').getall()))
#        for colour in colours:
#            colour_num = colour.rpartition('/')[2].rsplit('.')[0]
#            colour_desc = response.css('.colors a img[src="%s"]::attr(alt)' % colour).get()
#            cols[colour_num] = colour_desc

        for href in response.css('.product-landing-product-block-color > div > a::attr(href)').getall():
            url = response.urljoin(href)
            req = scrapy.Request(url, callback = self.parse_product_page)
            yield req

    def parse_product_page(self, response):
        yield {
            'item_url': response.url
            }

#    def parse_product_page2(self, response):
#
#        global cols
#
#        item_link = response.url
#        item_colour_num = item_link.rsplit('=')[1]
#        item_colour_desc = cols[item_colour_num]
#
#        item_num_name = (' '.join(response.css('h1::text').getall())).strip()
#        item_num = item_num_name.partition(' ')[0]
#        item_name = item_num_name.partition(' ')[2]
#
#        image_urls = []
#        for href in response.css('.img.zoom-container a[id="zoom-target"]::attr(href)').getall():
#            image_url = response.urljoin(href)
#            image_urls.append(image_url)
#
#        yield {
#            'item_num': item_num,
#            'item_name': item_name,
#            'item_colour_num': item_colour_num,
#            'item_colour_desc': item_colour_desc,
#            'item_link' : item_link,
#            'item_desc' : response.css('p.intro::text').getall(),
#            'item_features' : response.css('.p-c ul li::text').getall(),
#            'item_sizes' : response.css('.p-c  p:nth-of-type(2)::text').getall(),
#            'item_addl_info' : response.css('.symbols.cf a img::attr(alt)').getall(),
#            'image_urls': image_urls
#        }
