# -*- coding: utf-8 -*-
import scrapy


class RegattaSpider(scrapy.Spider):
    name = 'regatta'
    download_delay = 1
    allowed_domains = ['www.regattaprofessional.com']
    start_urls = ['http://www.regattaprofessional.com/regatta-professional-range.aspx',
    #start_urls = ['http://www.regattaprofessional.com/tacticalthreads-range.aspx',
#                  'http://www.regattaprofessional.com/tacticalthreads-range.aspx',
#                  'http://www.regattaprofessional.com/activewear-range.aspx',
#                  'http://www.regattaprofessional.com/originals-range.aspx']
    ]

#    custom_settings = {
#        'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 100,
    #                       'heaver.pipelines.HeaverMysqlPipeline': 200,
#        }
#    }

#    def parse_start_url(response):
#        if response.url = 'http://www.regattaprofessional.com/regatta-professional-range.aspx':
#            parse_regatta_professional(response)
#        if response.url = 'http://www.regattaprofessional.com/tacticalthreads-range.aspx':
#            parse_tactical_threads(response):

    def parse(self, response):
        for href in response.css('.section.group > .col.span_1_of_2 a::attr(href)').getall():
            url = response.urljoin(href)
            req = scrapy.Request(url, callback = self.parse_sections)
            yield req


    def parse_sections(self, response):
        item_nums = response.css('.catItem::attr(alt)').getall()
        for item_num in item_nums:
            url = 'http://www.regattaprofessional.com/product-detail.aspx?part_number=%s' % item_num
            req=scrapy.Request(url, callback = self.parse_product_page)
            yield req

    def parse_product_page(self, response):
        item_url = response.url
        yield {
            'item_url': item_url
        }
