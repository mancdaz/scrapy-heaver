#!/usr/bin/env python

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "snickers2"

    start_urls = [
        'http://www.snickersworkwear.co.uk/workwear/?items-per-page=all',
    ]

    def parse(self, response):
        for href in response.css('.product .colors a::attr(href)').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback = self.parse_product_page)


    def parse_product_page(self, response):
        yield {
            'item_name' : response.css('h1::text').extract(),
            'item_desc' : response.css('p.intro::text').extract(),
            'item_features' : response.css('.p-c ul li::text').extract(),
            #'item_sizes' : ,
        }
