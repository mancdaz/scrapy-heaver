import scrapy
import requests
from scrapy_splash import SplashRequest
import json
import re


# class QuotesSpider(scrapy.Spider):
#     name = "blaklader_test"
#     start_urls = [
#         'https://www.blaklader.uk/en/product/34581760-flame-retardant-sweatshirt#8933'
#     ]
#     for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         for quote in response.css('main.cd-main-content'):
#             yield {
#                 'vat': quote.css('span.vat::text').get()
#             }



class QuotesSpider(scrapy.Spider):
    name = "blaklader_bckup"
    # start_urls = ['https://www.blaklader.uk/en/products/all-products/ListProducts?c=&q=&flags=&sortorder=5&query=&page=1&pageSize=12&filters=']
    start_urls = [
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=1&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=2&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=3&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=4&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=5&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=6&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=7&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=8&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=9&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=10&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=11&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=12&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=13&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=14&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=15&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=16&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=17&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=18&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=19&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=20&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=21&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=22&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=23&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=24&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=25&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=26&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=27&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=28&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=29&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=30&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=31&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=32&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=33&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=34&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=35&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=36&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=37&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=38&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=39&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=40&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=41&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=42&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=43&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=44&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=45&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=46&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=47&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=48&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=49&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=50&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=51&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=52&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=53&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=54&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=55&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=56&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=57&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=58&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=59&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=60&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=61&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=62&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=63&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=64&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=65&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=66&pageSize=12&filters=',
        'https://www.blaklader.fr/fr/produits/tous-les-produits/ListProducts?c=&q=&flags=&sortorder=5&query=&page=67&pageSize=12&filters='


        

    ]
    # base_url = 'https://www.blaklader.uk/en/products/all-products/ListProducts?c=&q=&flags=&sortorder=5&query=&page=%s&pageSize=12&filters='
    # start_urls = [base_url %1]
    download_delay = 5

    
    def parse(self, response):
        
        global cols
        global prodCols
        global prodInfo
        global prodVars
        data = json.loads(response.body)
        for product in data.get('Products', []):
            prodCols=[]
            prodInfo=[]
            prodVars = []
            url=""
            item_name=""
            item_unique_name=""
            item_sizes=""
            url = product.get('Url')
            url = "https://www.blaklader.fr" + url
            # print("PRINT URL: " + url)

            item_name = product.get('Name')
            item_unique_name = product.get('UniqueName')
            url = url
            item_sizes = product.get('SizeSpan')
            rrp = product.get('ColorVariants')[0].get('PriceNew')
            
            prodInfo.append([item_name,item_unique_name,item_sizes,rrp])

            for colVariant in product["ColorVariants"]:
                image_url = colVariant.get('ColorParametricNew').get('ImageUrl')
                colour = colVariant.get('ColorParametricNew').get('Value')
                colour_code = colVariant.get('ColorParametricNew').get('Code')
                col_id = colVariant.get('ColorParametricNew').get('Id')
                # cols[colour_code] = colour
                prodCols.append([colour_code,colour,image_url,col_id])
                key = 'variant_code'
                prodVars.append(str(col_id))

            # req = SplashRequest(url, callback = self.parse_product_page,endpoint='render.html', args={'wait': 0.5})
            req = scrapy.Request(url,callback = self.parse_product_page, meta={
                'scrapy_splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}}})
            req.meta['prodCols'] = prodCols
            req.meta['prodInfo'] = prodInfo
            req.meta['prodVars'] = prodVars
            yield req

            # if data['has_next']:
            #     next_page = data['page'] + 1
            #     yield scrapy.parse(self.quotes_base_url % next_page)
        # get all colors and convert to names and pop in a dict for lookup
        # later
        # colours = list(set(response.css('.colors a img::attr(src)').getall()))
        # for colour in colours:
        #     colour_num = colour.rpartition('/')[2].rsplit('.')[0]
        #     colour_desc = response.css('.colors a img[src="%s"]::attr(alt)' % colour).get()
        #     cols[colour_num] = colour_desc

        # for href in response.css('#product-list-wrapper > ul > li:nth-child(2) > div.row.product-list-item.is-flex.vertical-align-center > a::attr('href')'):
        # for href in response.selector.xpath('//*[@id="product-list-wrapper"]/ul/li[2]/div[4]/a/@href').getall()
        # all_links = response.xpath('//*[@id="product-list-wrapper"]/ul/li[2]/div[4]/a')
        
        # for link in all_links:    
        #     url = response.urljoin(link)
        #     print("URL = " + href)
        #     # yield SplashRequest(url, callback = self.parse_product_page,endpoint='render.html', args={'wait': 0.5})
        #     yield scrapy.Request(url, callback = self.parse_product_page)

        # for href in response.css('#product-list-wrapper > ul > li:nth-child(2) > div.row.product-list-item.is-flex.vertical-align-center > a::attr(href)').extract():
        #     url = response.urljoin(href)
        #     print("URL ==== " + url)
        #     req = scrapy.Request(url, callback = self.parse_product_page)
        #     yield req
            
        
    def parse_product_page(self, response):
        
        global sizeList

        product = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % product
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        prodCols = response.meta.get('prodCols')
        prodInfo = response.meta.get('prodInfo')
        prodVars = response.meta.get('prodVars')
        # global cols
        # global prodCols
        # global prodInfo
        item_link = response.url
        print('item link is %s: ' % item_link)

        #item_colour_num = item_link.rsplit('=')[1]
        # item_colour_desc = cols[item_colour_num]
        # name = response.selector.xpath('/html/head/title/text()').get()
        # name = name.strip()
        # name = name[:name.index("(")]
        # print(name)
        separator = '. '

        qw2 = response.selector.xpath('//*[@id="product-page-tabs-content-description"]/div/text()').getall()
        qw2 = " ".join(x.strip() for x in qw2) 
        print("XXXX: " + qw2)

        # if qw2:
        #     print("STRIP1: " + qw2)
        #     qw2.strip('\r\n')
        #     print("STRIP2: " + qw2)
            # qw2.lstrip('\r\n')
        # print(qw2)

        # function_html = response.selector.xpath('//*[@id="product-page-tabs-function"]/div').getall()
        # function = response.selector.xpath('//*[@id="product-page-tabs-function"]/div/span/text()').getall()

        function_html = response.selector.xpath('//*[@id="product-page-tabs-function"]/div[normalize-space(.)]').getall()
        function = response.selector.xpath('//*[@id="product-page-tabs-function"]/div/span/text()[normalize-space(.)]').getall()
        
        if function:
            function = separator.join(function)
            function.strip('\r\n')
            function = re.sub('<.*?>', ' ', function)
        # print("Function: " + function)


        # function_bs = BeautifulSoup(function_html,'html.parser')
        # function = function_bs.get_text()
        # function=str(function_html[0])
        # if function != "":
        #     function.strip('\r\n')
        #     function = re.sub('<.*?>', ' ', function)

        # print("Function: " + function)

        washing=response.selector.xpath('//*[@id="product-page-tabs-content-description"]/div/div/img/@alt').getall()
        washing = separator.join(washing)
        certifications = response.selector.xpath('//*[@id="product-page-tabs-content-certs"]/div/p/text()[normalize-space(.)]').getall()
        certificationstring = str('.'.join(certifications).strip('\r\t\n'))
        certificationstring.replace('\r\n','')
        

        # certifications = separator.join(certifications)
        # certifications.strip('\r\n')
        # if certifications != "":
        #     certifications = separator.join(certifications)
        #     certifications = certifications.strip()
        description = response.selector.xpath('//*[@id="product-description-wrapper"]/div/div/p/text()[normalize-space(.)]').getall()
        # if description != "":
        #     description = description.strip()
        item_product_code = response.css('main [id=Sku]::attr(value)').get()
        blank = ""
        
        # updated_list = []

        # sub_item = {}
        # sub_item['Product']
        # sub_item['Product']['Code'] = item_product_code
        # sub_item['Product']['URL'] = item_link
        # sub_item['Product']['Name'] = prodInfo[0][0]
        # sub_item['Product']['UniqueName'] = prodInfo[0][1]
        # sub_item['Product']['Sizes'] = prodInfo[0][2]
        # sub_item['Product']['RRPExVAT'] = prodInfo[0][3]
        # sub_item['Product']['Description'] = description
        # sub_item['Product']['FunctionalityHTML'] = function_html
        # sub_item['Product']['FunctionalityText'] = function
        # sub_item['Product']['Certifications'] = certificationstring
        # sub_item['Product']['Quality1'] = response.selector.xpath('//*[@id="product-page-tabs-content-description"]/div/p/text()').getall()
        # sub_item['Product']['Quality2'] = qw2
        # sub_item['Product']['WashingInstructions'] = washing
        # sub_item['Product']['Images'] = response.selector.xpath('//*[@id="product-files-list"]/li/a/@href').getall()
        # sub_item['Product']['Video'] = response.css('#product-page-video-item > video > source::attr(src)').extract()
        # }

        prodVarsString = ""
        prodVarsString = ",".join(prodVars)
        print("PRODVARSSTRING: " + prodVarsString)

 


        yield {
            'product_code' : item_product_code,
            'product_variant_id' : blank,
            'product_url' : item_link,
            'product_name' : prodInfo[0][0],
            'product_unique_name' : prodInfo[0][1],
            'variant_code' : blank,
            'variant_colour_code' : blank,
            'variant_colour_name' : blank,
            'product_sizes' : prodInfo[0][2],
            'product_rrp_ex_vat' : prodInfo[0][3],
            'product_desc' : description,
            'product_function_html' : function_html,
            'product_function' : function,
            'product_certifications' : certificationstring,
            'product_quality&washing_1' : response.selector.xpath('//*[@id="product-page-tabs-content-description"]/div/p/text()').getall(),
            'product_quality&washing_2' : qw2,
            'product_quality&washing_3' : washing,
            'product_image_urls' : response.selector.xpath('//*[@id="product-files-list"]/li/a/@href').getall(),
            'variant_image' : blank,
            'product_image_vid' : response.css('#product-page-video-item > video > source::attr(src)').extract(),
            'product_variants' :  prodVarsString
        }

        i=0
        while i < len(prodCols):
            item_prod_id = response.css('main [id=Sku]::attr(value)').get() + prodCols[i][0]
            # sub_item1={}
            # sub_item1['ColourVariant'] = {}
            # sub_item1['ColourVariant']['Id'] = item_prod_id
            # sub_item1['ColourVariant']['Colour'] = prodCols[i][1]
            # sub_item1['ColourVariant']['Code'] = prodCols[i][0]
            # sub_item1['ColourVariant']['Image'] = prodCols[i][2]

            yield {
                'product_code' : blank,
                'product_variant_id' : blank,
                'product_url' : blank,
                'product_name' : blank,
                'product_unique_name' : blank,
                'variant_code' : item_prod_id,
                'variant_colour_code' : prodCols[i][0],
                'variant_colour_name' : prodCols[i][1],
                'product_sizes' : prodInfo[0][2],
                'product_rrp_ex_vat' : blank,
                'product_desc' : blank,
                'product_function_html' : blank,
                'product_function' : blank,
                'product_certifications' : blank,
                'product_quality&washing_1' : blank,
                'product_quality&washing_2' : blank,
                'product_quality&washing_3' : blank,
                'product_image_urls' : blank,
                'variant_image' : prodCols[i][2],
                'product_image_vid' : blank,
                'product_variants' :  prodVarsString
            }



            # yield {
            #     'variant_colour_id' : prodCols[i][3],
            #     'variant_code' : item_prod_id,
                # 'item_link' : blank,
                # 'item_name' : prodInfo[0][0],
                # 'item_unique_name' : prodInfo[0][1],
                # 'url' : url,
                # 'item_sizes' : prodInfo[0][2],
                # 'variant_colour_code' : prodCols[i][0],
                # 'variant_colour_name' : prodCols[i][1],
                # 'rrp_ex_vat' : blank,
                # 'item_color_num': item_colour_num
                # 'item_colour_desc': item_colour_desc,
                # 'item_sizes' : response.css('.p-c  p:nth-of-type(2)::text').get(),
                # 'item_desc' : blank,
                # 'item_function_html' : blank,
                # 'item_function' : blank,
                # 'item_certifications' : blank,
                # 'item_quality&washing_1' : blank,
                # 'item_quality&washing_2' : blank,
                # 'item_quality&washing_3' : blank,
                # 'image_urls' : blank,
                # 'variant_image' : prodCols[i][2],
                # 'product_code' : item_product_code
                # 'image_vid' : blank   

            # }
            i+=1
        

        # updated_list.append(sub_item)
        # return updated_list






