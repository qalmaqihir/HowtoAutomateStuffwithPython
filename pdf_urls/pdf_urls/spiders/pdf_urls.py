from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from pdf_urls.items import  PdfUrlsItem


# CrawlSpinder or scrapy.spider can be used
class PdfUrlSpider(CrawlSpider):
    # This nameis required. it is how we refer to this PdfUrlSpider class from commnd line
    name = 'pdf_urls'
    # Every link we look at MUST be a part of the adobe.com domain (i.e contains "adobe.com" in it's url)
    allowed_domains=['ucentralasia.org']
    # this is the url we will start from (check all the links on this webpage first and then go deeper
    start_urls=['https://ucentralasia.org']
    # this Rule Says:
    # 1. allow all links to be extracted
    # 2. call parse_httpresponse on each extracteed link
    # 3. follow all links ("click" on them) so we can check all links on THAT webpage too
    # rules=[scrapy.spiders.Rule(link_extractor='',callback='parse_httpresponse',follow=True)]
    rules=[Rule(LinkExtractor(allow=''),callback='parse_httpresponse',follow=True)]


    def parse_httpresponse(self, response):
        if response.status!=200:
            return None

        # print(response)
        print(response.url)
        # print(response.headers)
        # print(type(response.headers))
        # print(type(dict(response.headers)))
        # print(response.headers.keys())
        # print(response.headers['Content-Type'])

        item = PdfUrlsItem()
        #
        # # # check if the link goes to pdf
        link_to_pdf = 'application/pdf' in str(response.headers['Content-Type'])
        print(link_to_pdf)
        print(response.url.split('/')[-1])
        # to avoid error and crash of our progeam if the key is not presnt,
        if b'Content-Type' in response.headers.keys():
            link_to_pdf = 'application/pdf' in str(response.headers['Content-Type']) # check out https://iana.org/assignments/media-types/media-types.xhtml for other files types
            # print(link_to_pdf)
        else:
            return None

        print(str(response.headers['Content-Type']))
        # if so then scrape it
        # check if content-disposition exits
        content_disposition_exists=b'Content-Disposition' in response.headers.keys()
        print(content_disposition_exists)

        if link_to_pdf:
            # scrapy the specified data
            if content_disposition_exists:
                item['url']=response.url
                s=str(response.headers['Content-Disposition'])
                item['filename']=re.search('filename="(.+)',s).group(1)

            else:
                item['url']=response.url
                item['filename']=response.url.split('/')[-1] # Use a file name (attchement name) from the header

        else:
            return None

        # if not, ignor it and move on to the next lin
        # write that data to the csv
        return item



