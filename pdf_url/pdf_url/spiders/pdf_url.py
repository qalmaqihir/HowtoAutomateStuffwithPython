from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# CrawlSpinder or scrapy.spider can be used
class PdfUrlSpider(CrawlSpider):
    # This nameis required. it is how we refer to this PdfUrlSpider class from commnd line
    name = 'pdf_url'
    # Every link we look at MUST be a part of the adobe.com domain (i.e contains "adobe.com" in it's url)
    allowed_domains=['adobe.com']
    # this is the url we will start from (check all the links on this webpage first and then go deeper
    start_urls=['https://www.adobe.come']
    # this Rule Says:
    # 1. allow all links to be extracted
    # 2. call parse_httpresponse on each extracteed link
    # 3. follow all links ("click" on them) so we can check all links on THAT webpage too
    # rules=[scrapy.spiders.Rule(link_extractor='',callback='parse_httpresponse',follow=True)]
    rules=[Rule(LinkExtractor(allow=''),callback='parse_httpresponse',follow=True)]


    def parse_httpresponse(self, response):
        print(response)
        # print(response.url)
        # print(response.headers)
        # print(type(response.header))
        # print(type(dict(response.header)))
        # print(response.header.keys())
        # print(response.header['Content-Type'])

        # item = PdfUrlItem()

        # check if the link goes to pdf

        # if so then scrape it
        # if not, ignor it and move on to the next lin
        # write that data to the csv

        return


