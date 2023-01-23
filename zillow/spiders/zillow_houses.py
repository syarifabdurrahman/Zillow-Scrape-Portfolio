import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, COOKIE, cookie_parser, parse_new_url
from ..items import ZillowItem
import json


class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']
    start_urls = [URL]

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            cookies=cookie_parser(COOKIE),
            callback=self.parse,
            meta={
                'currentPage': 1
            }
        )

    def parse(self, response):
        # print(response.body)

        # with open('initial_response.json','wb') as file:
        #     file.write(response.body)
        current_page = response.meta['currentPage']
        json_resp = json.loads(response.body)
        # print(json_resp)

        houses = json_resp.get('cat1').get('searchResults').get('listResults')

        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', house.get('id'))
            loader.add_value('image_urls', house.get('imgSrc'))
            loader.add_value('detail_url', house.get('detailUrl'))
            loader.add_value('status_type', house.get('statusType'))
            loader.add_value('status_text', house.get('statusText'))
            loader.add_value('price', house.get('price'))
            loader.add_value('address', house.get('address'))
            loader.add_value('beds', house.get('beds'))
            loader.add_value('baths', house.get('baths'))
            loader.add_value('area_sqrft', house.get('area'))
            loader.add_value('latetitude', house.get(
                'latLong').get('latitude'))
            loader.add_value('longitude', house.get(
                'latLong').get('longitude'))
            loader.add_value('broker_name', house.get('brokerName'))
            # loader.add_value('broker_phone',house.get('id'))

            yield loader.load_item()

        total_pages = json_resp.get('cat1').get('searchList').get('totalPages')

        if current_page <= total_pages:
            current_page += 1
            yield scrapy.Request(
                parse_new_url(url=URL, next_page_number=current_page),
                callback=self.parse,
                cookies=cookie_parser(COOKIE),
                meta={
                    'currentPage': current_page
                }
            )
