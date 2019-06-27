# -*- coding: utf-8 -*-
import scrapy


class SnickersSpider(scrapy.Spider):
    name = 'snickers'
    allowed_domains = ['http://www.snickersworkwear.co.uk/workwear/?items-per-page=all']
    start_urls = ['http://http://www.snickersworkwear.co.uk/workwear/?items-per-page=all/']

    def parse(self, response):
        pass
