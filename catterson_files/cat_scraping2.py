__author__ = 'adcat'

#from lxml import html
#import requests

#r = requests.get('http://www.drudgereportarchives.com/')
#print 'status:', r.status_code
#print 'initial text:', r.text[:4000]
#tree = html.fromstring(r.text)
#print tree.body.text_content()

#url_DR = ['http://www.drudgereportarchives.com/data/2014/08/21/20140821_014042.htm',
#          'http://www.drudgereportarchives.com/data/2014/08/21/20140821_014223.htm']

import scrapy

class Headline(scrapy.Item):
    url = scrapy.Field()
    main = scrapy.Field()

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class DrudgeSpider(CrawlSpider):

    name = 'drudgearch'
    allowed_domains = ['drudgereportarchives.com']
    start_urls = ['http://www.drudgereportarchives.com/data/2014/08']
    rules = [Rule(LinkExtractor(allow=['/21/\d+']), 'parse_html')]

    def parse_html(self, response):
        html = Headline()
        html['url'] = response.url
        return html

scrapy crawl drudgearch -o scraped_data.csv