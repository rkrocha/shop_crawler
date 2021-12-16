import scrapy
import datetime
from .kabum import KABUM_PAGES


class KabumSpider(scrapy.Spider):
    name = 'kabum'
    allowed_domains = ['www.kabum.com.br/']
    start_urls = [key for key in KABUM_PAGES]

    def parse(self, response):
        date = datetime.datetime.now()

        for product in response.xpath("//div[@id='listingOrdenation']/following::main/div[contains(@class, 'productCard')]/a"):
            price = product.xpath("./descendant::span[contains(@class, 'priceCard')]/text()").get()
            if '---' in price:
                break

            doc = {}
            doc['shop'] = "Kabum"
            doc['type'] = KABUM_PAGES[response.url]
            doc['title'] = product.xpath("./descendant::h2/text()").get()
            doc['url'] = "www.kabum.com.br" + product.xpath("./@href").get()

            info = {}
            info['price'] = float(''.join(char for char in price if char.isdigit())) / 100 # mover conversão de tipo para o pipeline
            info['date'] = date

            doc['info'] = info

            yield doc

"""
{
    "shop": "",
    "type": "",
    "title": "",
    "url": "",
    "info":
    {
        "date": datetime.datetime(),
        "price": 0.0,
    }
}
"""
