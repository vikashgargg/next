# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy.crawler import CrawlerProcess
# from scrapy import Request
# from urllib.parse import urlparse
# #import tldextract

# class LkSpider(CrawlSpider):
#     name = 'multi_spider'

#     # read csv with just url per line
#     with open('a.csv') as file:

#         start_urls = ["https://www.upcitemdb.com/upc/"+line.strip() for line in file]
#         print(start_urls)

#     def start_request(self):
#         for link in self.start_urls:
#             request = Request(url = self.start_urls, callback=self.parse)
#             yield request
 

#     rules = (
#         Rule(LinkExtractor(), callback='parse_item', follow=True),
#     )

#     def parse_item(self, response):
#         yield
#         {
#             'links': response.xpath('//table[@class="list"]/a/@href').getall(),
#         }

#         # get the domain for the file name
#         # domain = tldextract.extract(response.request.url)[1]
#         # path = urlparse(response.request.url)[2].replace("/", "")

#         # descriptions = response.xpath('*//p/text()').getall()
#         # description = ''.join(descriptions)
#         # description = description[:1200]
#         # filename = response.url.split("/")[-2] + '.txt'
#         # with open("output/" + domain + "_" + filename, 'w') as f:
#         #     f.write(description)

        

# # main driver
# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(LkSpider)
#     process.start()