# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from itemadapter import ItemAdapter


class MongoPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient('mongodb://storage:27017')
        self.collection = self.client.products.entries

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        product = ItemAdapter(item)
        self.collection.find_one_and_update({'_id': product['_id']},
                        {'$push': {'info': product['info'][0]}}, upsert=True)
        return item
