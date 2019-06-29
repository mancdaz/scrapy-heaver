#!/usr/bin/env python

import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "snickers"

    start_urls = [
        'http://www.snickersworkwear.co.uk/workwear/?items-per-page=all',
    ]

    def parse(self, response):

        # get all colors and convert to names and pop in a dict for lookup
        # later
        colours = list(set(response.css('.colors img::attr(title)').getall()))
        cols = {}
        for colour in colours:
            if colour:
                m = re.match(r"([0-9]*)(.+)", colour)
                col_num = m.groups()[0]
                col_desc = m.groups()[1]
                cols[col_num] = col_desc
        #print(cols)

        for href in response.css('.product .colors a::attr(href)').extract():
            url = response.urljoin(href)
            req = scrapy.Request(url, callback = self.parse_product_page)
            req.meta['item_link'] = url
            req.meta['cols'] = cols
            yield req


    def parse_product_page(self, response):
        #print(response.meta.get('cols'))
        yield {
            'item_link' : response.meta.get('item_link'),
            'item_name' : response.css('h1::text').extract(),
            'item_desc' : response.css('p.intro::text').extract(),
            'item_features' : response.css('.p-c ul li::text').extract(),
            #'item_sizes' : ,
        }
