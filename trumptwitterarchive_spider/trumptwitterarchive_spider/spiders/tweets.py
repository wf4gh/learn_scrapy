# -*- coding: utf-8 -*-
import scrapy
import json


class TweetsSpider(scrapy.Spider):
    name = 'tweets'
    allowed_domains = ['trumptwitterarchive.com']
    start_urls = ['http://www.trumptwitterarchive.com/data/realdonaldtrump/2019.json',
                  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2018.json']

    def parse(self, response):
        jsonresponse = json.loads(response.body)

        for tweet in jsonresponse:
            yield {
                'source': tweet['source'],
                'id_str': tweet['id_str'],
                'text': tweet['text'],
                'created_at': tweet['created_at'],
                'retweet_count': tweet['retweet_count'],
                'in_reply_to_user_id_str': tweet['in_reply_to_user_id_str'],
                'favorite_count': tweet['favorite_count'],
                'is_retweet': tweet['is_retweet']
            }
