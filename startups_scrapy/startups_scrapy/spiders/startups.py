import json

import scrapy


class Startups(scrapy.Spider):
    name = "startups"
    allow_domain = "sea.500.co"
    start_urls = [
        'https://sea.500.co/!/airtable-integration/portfolio?platform=&region=&sector=',
    ]

    def parse(self, response):
        data = json.loads(response.body)

        yield from data['data']

        nextPage = data['next']

        if nextPage is not None:
            yield scrapy.Request(nextPage, callback=self.parse)
