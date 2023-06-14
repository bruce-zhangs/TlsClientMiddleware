import logging

import scrapy


class TestSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-apikey': 'iphoneap',
            'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2'
        }
        for i in range(3):
            yield scrapy.Request(url="https://www.yogiyo.co.kr/api/v1/restaurants/128/?lat=0&lng=0", headers=headers, dont_filter=True)

    def parse(self, response):
        logging.info('get response')
        print(response.text)