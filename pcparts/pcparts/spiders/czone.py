from itemloaders.processors import MapCompose, TakeFirst
from pcparts.items import PcpartsItem
from scrapy.loader import ItemLoader
from urllib.parse import urljoin
from operator import methodcaller
import scrapy


strip = methodcaller('strip')

CATEGORY_SELECTOR = ".megamenu-content .child a::attr(href)"

BRAND_SELECTOR = "#spnBrand::text"
TITLE_SELECTOR = "#spnProductName::text"
STOCK_SELECTOR = "#spnStockStatus::text"
PRICE_SELECTOR = "#spnCurrentPrice::text"
RATING_SELECTOR = "#spnProductRating::text"
DESCRIPTION_SELECTOR = "#divProductDesc::text"
MEDIA_SELECTOR = "div.Div1.zoomWrapper img::text"


class CzoneSpider(scrapy.Spider):
    name = "czone"
    allowed_domains = ["czone.com.pk"]
    start_urls = ["https://www.czone.com.pk/laptops-acer-laptops-acer-aspire-5-a515-58p-33zm-laptop-13th-gen-intel-core-i3-1315u-8gb-512gb-ssd-15-6-fhd-windows-11-local-warranty-nx-khjsg-008-pakistan-p.14702.aspx"]

    # def parse(self, response):
    #     for anchor in response.css(CATEGORY_SELECTOR):
    #         url = urljoin(response.url, anchor.get())
    #         yield scrapy.Request(url=url, callback=self.parse_item)

    def parse(self, response):
        l = ItemLoader(item=PcpartsItem(), selector=response)

        l.add_css("title", TITLE_SELECTOR, MapCompose(strip,), TakeFirst(),)
        l.add_css("brand", BRAND_SELECTOR, MapCompose(strip,), TakeFirst(),)
        l.add_css("price", PRICE_SELECTOR, MapCompose(strip,), TakeFirst(),)
        l.add_css("media", MEDIA_SELECTOR, MapCompose(strip,), TakeFirst(),)
        l.add_css("rating", RATING_SELECTOR, MapCompose(strip,), TakeFirst(),)
        l.add_css("in_stock", STOCK_SELECTOR, MapCompose(strip,), TakeFirst(),)
        l.add_css("description", DESCRIPTION_SELECTOR,
                  MapCompose(strip,), TakeFirst(),)

        return l.load_item()
