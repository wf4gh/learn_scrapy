# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        #yield {'tags': tags}
        quotes = response.xpath('//*[@class="quote"]')
        for q in quotes:
            text = q.xpath('.//*[@class="text"]/text()').extract_first()
            author = q.xpath('//*[@class="author"]/text()').extract_first()
            keywords = q.xpath('//*[@class="keywords"]/@content').extract_first()
            yield {"text": text, "author": author, "keywords": keywords}
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        abs_next_page_url = response.urljoin(next_page_url) 
        yield scrapy.Request(abs_next_page_url) 
