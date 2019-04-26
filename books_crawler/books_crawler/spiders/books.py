# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
import os
import csv
import glob
import MySQLdb


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)
            
    def parse_book(self, response):
        title = response.xpath('//h1/text()').extract_first()
        rating = response.xpath(
            '//*[contains(@class, "star-rating")]/@class').extract_first().replace('star-rating ', '')

        def product_info(response, value):
            return response.xpath('//th[text()="{}"]/following-sibling::td/text()'.format(value)).extract_first()

        upc = product_info(response, 'UPC')
        product_type = product_info(response, 'Product Type')

        yield {
            'title': title,
            'rating': rating,
            'upc': upc,
            'product_type': product_type
        }
