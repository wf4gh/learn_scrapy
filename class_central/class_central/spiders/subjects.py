# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath(
                '//a[@class="text--blue" and contains(@title, "{}")]/@href'.format(self.subject)).extract_first()
            yield Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            self.logger.info('Scraping all subjects.')
            subjects = response.xpath(
                '//a[@class="text--blue"]/@href').extract()
            for subject in subjects:
                yield Request(response.urljoin(subject), callback=self.parse_subject)

    def parse_subject(self, response):
        subject_name = response.xpath(
            '//strong[@class="head-2 medium-up-head-1 text--bold"]/text()').extract_first()
        courses = response.xpath(
            '//a[@class="text--charcoal text-2 medium-up-text-1 block course-name"]')

        for course in courses:
            course_name = course.xpath('.//@title').extract_first()
            course_url = course.xpath('.//@href').extract_first()
            absolute_course_url = response.urljoin(course_url)

            yield {
                'subject_name': subject_name,
                'course_name': course_name,
                'absolute_course_url': absolute_course_url
            }

        next_page = response.xpath('//link[@rel="next"]/@href').extract_first(
        absolute_next_page=response.urljoin(next_page)
        yield Request(absolute_next_page, callback=self.parse_subject)
