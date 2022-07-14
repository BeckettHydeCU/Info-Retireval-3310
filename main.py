import scrapy

class SearchSpider(scrapy.Spider):
    name = "search"

    def start_requests(self):
        start_urls = ['https://www.colorado.edu/']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')