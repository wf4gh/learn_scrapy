# -*- coding: utf-8 -*-
import scrapy


class CrunchbaseSpider(scrapy.Spider):
    name = 'crunchbase'
    allowed_domains = ['crunchbase.com']
    start_urls = ['https://www.crunchbase.com/organization/medical-body-sculpting#section-overview']

    def parse(self, response):
        pass
