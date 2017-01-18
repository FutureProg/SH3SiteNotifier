import scrapy

class AnnounceSpider(scrapy.Spider):
    name = "announce"
    start_urls = ["http://www.cas.mcmaster.ca/~pophlin/teaching/cs3sh3/announcements.html"]

    def parse(self,response):
        counter = 0
        for item in response.xpath("//li//text()").extract():
            yield {"content":item}
            counter += 1
