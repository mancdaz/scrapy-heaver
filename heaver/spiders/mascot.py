#!/usr/bin/env python

import scrapy
import re

cols = {}

class MascotSpider(scrapy.Spider):
    name = "mascot"

    start_urls = [
        'https://www.mascotworkwear.co.uk/en/assortment#ss=*&mpt=&pt=&sb=&f=&mf=&mc=&pr=&q=&ce=&mce=&si=&mis=&hc=&p=&at=Clothes',
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
