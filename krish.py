# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# from tutorial.items import KrisItem
# from itemloaders.processors import MapCompose
# from scrapy.loader import ItemLoader

# def get_num(string):
#     return ''.join( i for i in string if i.isdigit() or i in ['.'])

# def get_prices(ls):
#     ls = [get_num(l) for l in ls]
#     return min(ls,default='0'),max(ls,default='0')

# class WnsSpider(CrawlSpider):
#     name = 'kris'
#     allowed_domains = ['krisshop.com']
#     start_urls = ['https://www.krisshop.com/en/category/kso_online_wineSpirits_wine?category=kso_online_wineSpirits_wine&excludeBrandType=premium&page=1']

#     box_xpaths = ['//a[@class="productTile  productGridTilesItem"]','//a[@class="productTile productTileIsOutOfStock productGridTilesItem"]']
#     next_xpath = '//div[@class="paginationNextPage"]'


#     rules = (
#         Rule(LinkExtractor(restrict_xpaths=next_xpath)),
#         Rule(LinkExtractor(restrict_xpaths=box_xpaths),callback='parse')
#             )

#     def parse(self, response):
#         l = ItemLoader(item = KrisItem(), response = response)
#         l.add_value('url',response.url)
#         l.add_xpath('name','//div[@class="productHeaderTitleText"]/text()',MapCompose(str.strip))
#         l.add_xpath('brand','//a[@class="productHeaderBrandLink"]/text()',MapCompose(str.strip))
#         l.add_xpath('price','string(//div[@class="productPriceLine"])',MapCompose(get_num))
#         l.add_xpath('short_description','string(//div[@class="productHeaderDescription richtext"])',MapCompose(str.strip))
#         l.add_xpath('description','string(//div[@class="productDescriptionExpandable"])',MapCompose(str.strip))
#         l.add_xpath('oos','//p[@class="infoBoxContent"]/text()',MapCompose(str.strip))

#         return l.load_item()

