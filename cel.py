# import json
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# from tutorial.items import CellarbrationItem
# from itemloaders.processors import MapCompose
# from scrapy.loader import ItemLoader
# import pandas as pd

# def get_num(string):
#     return ''.join( i for i in string if i.isdigit() or i in ['.'])

# def get_table_as_json(string):
#     table = pd.read_html(string)[0]
#     table.index = table.iloc[:,0]
#     table = table.iloc[:,1]
#     table = table.to_dict()
#     return json.dumps(table)

# class CelSpider(CrawlSpider):
#     name = 'cel'
#     allowed_domains = ['cellarbration.com.sg']
#     start_urls = ['https://cellarbration.com.sg/all-wines.html']

#     box_xpath = '//div[@class="product photo product-item-photo"]/a'
#     #box_xpath =  '//div[@class="product-item-info type2"]'
#     next_xpath = '//a[@class="action  next"]'

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths=next_xpath)),
#         Rule(LinkExtractor(restrict_xpaths=box_xpath),callback='parse')
#             )

#     def parse(self, response):
#         l = ItemLoader(item = CellarbrationItem(), response = response)
#         l.add_value('url',response.url)
#         l.add_xpath('title','//span[@class="base"]/text()',MapCompose(str.strip))
#         l.add_xpath('regular_price','string(//span[@class="old-price"])',MapCompose(get_num))
#         l.add_xpath('sale_price','string(//span[@class="special-price"])',MapCompose(get_num))
#         l.add_xpath('short_description','string(//div[@itemprop="description"]/text())',MapCompose(str.strip))
#         l.add_xpath('description','string(//div[@id="description"])',MapCompose(str.strip))
#         l.add_xpath('table','//table[@id="product-attribute-specs-table"]',MapCompose(get_table_as_json))
#         l.add_xpath('oos','string(//div[@class="stock available"]/span[2]/text())',MapCompose(str.strip))
#         return l.load_item()

