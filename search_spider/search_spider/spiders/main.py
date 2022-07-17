import scrapy
import xml.etree.ElementTree as ET
from os.path import exists
import json

def write_json(data, filename="text-data.json"):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["data"].append(data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

class SearchSpider(scrapy.Spider):
    name = "search"

    def start_requests(self):
        if not exists("text-data.json"):
            with open("text-data.json", 'w') as file:
                file.write('{"data":[]}')
        start_urls = []
        print("Begin Parsing:")
        mytree = ET.parse('../sitemap.xml')
        myroot = mytree.getroot()
        for child in mytree.iter():
            #print(child.tag)
            if child.tag == "{http://www.sitemaps.org/schemas/sitemap/0.9}loc":
                print(child.text)
                start_urls.append(child.text)
        print("Parsing complete.")

        # start_urls = ['https://www.motherfuckingwebsite.com/']
        i = 0
        for url in start_urls:
            i += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'url': url, 'i': i})

    def parse(self, response):
        self.log("I : " + str(response.meta.get('i')))
        ignore_tags = ['.menu-icon-text']
        req_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'strong']
        section_selector = response.css('body')
        for section in section_selector:
            texts = []
            for tag in section.css('*'):
                if tag.root.tag in ignore_tags:
                    tag.root.getparent().remove(tag.root)
            for tag in section.css('*'):
                if tag.root.tag in req_tags:
                    texts = texts + tag.css('*::text').getall()
            write_json({"url": response.meta.get('url'), "texts": texts})
            
            self.log("logged")

        # page = response.url.split("/")[-2]
        # filename = f'spider-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')