import scrapy

class DocPython(scrapy.Spider):
    name = 'doc_python'
    allowed_domains = ['python.com']
    start_urls = [
        'https://docs.python.org/3/library/os.html',
    ]

    def parse(self, response):
        for h3 in response.xpath('//h3').getall():
            print(h3)
            yield {"title": h3}

        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
