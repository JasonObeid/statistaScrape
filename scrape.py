import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

Path = "scraped.csv"

class MySpider(scrapy.Spider):
    name = "ScraperWithLimit"
    start_urls = ['https://www.statista.com/markets/']
    allowed_domains = ['https://www.statista.com/markets/', 'https://www.statista.com/statistics/']
    custom_settings = {
        'DEPTH_LIMIT': 3
    }

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            if (link not in sr):
                url = link.url
                if ('https://www.statista.com/statistics/' in url):
                    print(link)
                    sr.append(link)
                yield response.follow(link, self.parse)


sr = []
process = CrawlerProcess()
process.crawl(MySpider)
process.start()
print(sr)

frame = pd.DataFrame(sr)
frame.to_csv(index=False, path_or_buf=Path)