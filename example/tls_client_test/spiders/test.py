import logging

import scrapy


class TestSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        params = {
            'limit': '18',
            'offset': '0',
        }
        met_data = {
            'params': params
        }
        for i in range(3):
            yield scrapy.Request(url="https://dynamic5.scrape.center/api/book/", headers=headers, dont_filter=True, meta=met_data)

    def parse(self, response):
        logging.info('get response')
        print(response.text)