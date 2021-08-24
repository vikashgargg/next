# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# from tutorial.items import AsherItem
# from itemloaders.processors import MapCompose
# from scrapy.loader import ItemLoader

# def get_num(string):
#     return ''.join( i for i in string if i.isdigit() or i in ['.'])

# def get_prices(ls):
#     ls = [get_num(l) for l in ls]
#     if len(ls) == 1:
#         return '0',ls[0]
#     else:
#         return min(ls,default='0'),max(ls,default='0')

# class AsherSpider(CrawlSpider):
#     name = 'asher'
#     allowed_domains = ['asherbws.com']
#     start_urls = ['https://www.asherbws.com/product-category/wine/']

#     box_xpath = '//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]'
#     next_xpath = '//a[@class="next page-numbers"]'

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths=next_xpath)),
#         Rule(LinkExtractor(restrict_xpaths=box_xpath),callback='parse')
#             )

#     def parse(self, response):
#         l = ItemLoader(item = AsherItem(), response = response)
#         l.add_value('url',response.url)
#         l.add_xpath('name','//h1[@class="product_title entry-title"]/text()',MapCompose(str.strip))
#         l.add_xpath('short_description','string(//div[@class="woocommerce-product-details__short-description"])',MapCompose(str.strip))
#         l.add_xpath('description','string(//div[@id="tab-description"])',MapCompose(str.strip))
#         l.add_xpath('brand','string(//span[@class="posted_in"]/a[last()])',MapCompose(str.strip))

#         prices = response.xpath('//p[@class="price"]//span[@class="woocommerce-Price-amount amount"]').getall()
#         prices = get_prices(prices)
#         l.add_value('regular_price',prices[0])
#         l.add_value('sale_price',prices[1])

#         return l.load_item()



import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
from tutorial.items import AsherItem
from itemloaders.processors import MapCompose
from scrapy.loader import ItemLoader
#from peye.utils import get_num

def get_num(string):
    num = ''.join( i for i in string if i.isdigit() or i in ['.'])
    try:
        num = float(num)
        return num
    except ValueError as e:
        return '-'

def get_prices(ls):
    ls = [get_num(l) for l in ls]
    if len(ls) == 1:
        return '0',ls[0]
    else:
        return min(ls,default='0'),max(ls,default='0')

class AsherSpider(Spider):
    name = 'asher'
    allowed_domains = ['asherbws.com']
    start_urls = ['https://www.asherbws.com/product-category/spirits/whisky/']

    start_urls_dict= [
            {'category' : 'whisky',
            'sub_category': 'american_whisky',
            'url':'https://www.asherbws.com/product-category/spirits/whisky/'
            },
            {'category' : 'wine',
            'sub_category': 'wine',
            'url':'https://www.asherbws.com/product-category/wine://www.asherbws.com/product-category/wine/'
            },
    ]

    box_xpath = '//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]'
    next_xpath = '//a[@class="next page-numbers"]'

    #rules = (
    #    Rule(LinkExtractor(restrict_xpaths=next_xpath)),
    #    Rule(LinkExtractor(restrict_xpaths=box_xpath),callback='parse')
    #        )

    def start_requests(self):
        for meta_dict in self.start_urls_dict:
            category = meta_dict.get('category','')
            sub_category = meta_dict['sub_category']
            products_page = meta_dict['url']
            yield scrapy.Request(products_page,callback=self.get_products,meta=meta_dict)


    def get_products(self, response):

        for link in LinkExtractor(restrict_xpaths=self.box_xpath).extract_links(response):
            yield scrapy.Request(link.url,callback=self.get_product,meta=response.meta)
        for link in LinkExtractor(restrict_xpaths=self.next_xpath).extract_links(response):
            yield scrapy.Request(link.url,callback=self.get_product,meta=response.meta)
    


    def get_product(self, response):
        l = ItemLoader(item = AsherItem(), response = response)
        l.add_value('product_link',response.url)
        l.add_xpath('product_name','//h1[@class="product_title entry-title"]/text()',MapCompose(str.strip))
        l.add_xpath('brand','string(//span[@class="posted_in"]/a[last()])',MapCompose(str.strip))

        prices = response.xpath('//p[@class="price"]//span[@class="woocommerce-Price-amount amount"]').getall()
        prices = get_prices(prices)
        l.add_value('regular_price',prices[0])
        l.add_value('sale_price',prices[1])

        l.add_value('business_name',self.name)
        l.add_value('category',response.meta['category'])
        l.add_value('sub_category',response.meta['sub_category'])


        desc1 = response.xpath('string(//div[@class="woocommerce-product-details__short-description"])').getall()
        desc2 = response.xpath('string(//div[@id="tab-description"])').getall()
        l.add_value('description',desc1 + desc2)

        return l.load_item()



# next_page_partial_url = response.xpath(
#                 '//li[@class="next"]/a/@href').extract_first()
#             next_page_url = self.base_url + next_page_partial_url
#             yield scrapy.Request(next_page_url, callback=self.get_product)


