#!/usr/bin/env python

import scrapy
import re

cols = {}

class QuotesSpider(scrapy.Spider):
    name = "snickers"

    start_urls = [
        'http://www.snickersworkwear.co.uk/workwear/?items-per-page=all',
    ]


    def parse(self, response):

        global cols

        # get all colors and convert to names and pop in a dict for lookup
        # later
        colours = list(set(response.css('.colors a img::attr(src)').getall()))
        for colour in colours:
            colour_num = colour.rpartition('/')[2].rsplit('.')[0]
            colour_desc = response.css('.colors a img[src="%s"]::attr(alt)' % colour).get()
            cols[colour_num] = colour_desc

        for href in response.css('.product .colors a::attr(href)').extract():
            url = response.urljoin(href)
            req = scrapy.Request(url, callback = self.parse_product_page)
            yield req


    def parse_product_page(self, response):

        global cols

        item_link = response.url
        print('item link is %s: ' % item_link)
        item_colour_num = item_link.rsplit('=')[1]
        item_colour_desc = cols[item_colour_num]

        item_num_name = (' '.join(response.css('h1::text').getall())).strip()
        item_num = item_num_name.partition(' ')[0]
        item_name = item_num_name.partition(' ')[2]

        yield {
            'item_num': item_num,
            'item_name': item_name,
            'item_color_num': item_colour_num,
            'item_colour_desc': item_colour_desc,
            'item_link' : item_link,
            'item_desc' : response.css('p.intro::text').extract(),
            'item_features' : response.css('.p-c ul li::text').extract(),
            'item_sizes' : response.css('.p-c  p:nth-of-type(2)::text').get(),
            'image_urls': response.css('.img.zoom-container a img::attr(src)').getall()
        }
