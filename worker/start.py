from scrapy import settings
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from pymongo import MongoClient
from time import sleep

# from queries import Queries
from kabum_spider import KabumSpider
from crawlers import settings as my_settings


crawler_settings = Settings()
crawler_settings.setmodule(my_settings)
process = CrawlerProcess(settings=crawler_settings)
process.crawl(KabumSpider)
process.start()

client = MongoClient('mongodb://storage:27017')
storage = client.products.entries
print(storage.count_documents({}))
print(storage.find_one({}))
client.close()

# docker compose up --abort-on-container-exit
