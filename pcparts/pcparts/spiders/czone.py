from urllib.parse import urljoin
import scrapy

CATEGORY_SELECTOR = ".megamenu-content .child a::attr(href)"


class CzoneSpider(scrapy.Spider):
    name = "czone"
    allowed_domains = ["czone.com.pk"]
    start_urls = ["http://czone.com.pk/"]

    def parse(self, response):
        for anchor in response.css(CATEGORY_SELECTOR):
            url = urljoin(response.url, anchor.get())
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        yield dict(title=response.xpath("//title/text()").get())
