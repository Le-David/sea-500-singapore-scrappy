import scrapy


class Startups(scrapy.Spider):
    name = "startups"
    allow_domain = "sea.500.co"
    start_urls = [
        'https://sea.500.co/!/airtable-integration/portfolio?region=Singapore&sector=&platform=',
    ]

    def parse(self, response):
        print(response.body)
        pass
