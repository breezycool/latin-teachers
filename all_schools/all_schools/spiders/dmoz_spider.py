import scrapy
from all_schools.items import LinkItem

scrapy.linkextractors import LinkExtractor

# each scrapyself.Spider child must have
#   - name
#   - start_urls
#   - parse()

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    domain = "http://www.privateschoolreview.com"
    allowed_domains = ["privateschoolreview.com"]
    start_urls = [
        'http://www.privateschoolreview.com/'
    ]

    # crawl original page for school lists
    def parse(self, response):
        # <div class="city_box"><ul><li>
        for sel in response.xpath('//div[@class="city_box"]/ul/li'):
            item = LinkItem()
            link_extension = sel.xpath('a/@href').extract()[0]
            item['link'] = self.domain + link_extension
            if item['link']:
                yield scrapy.Request(item['link'], callback=self.parse_state_region)

    # crawl each state region that contains a school list
    def parse_state_region(self, response):
        # <a class="school_links">
        for sel in response.xpath('//a[@class="school_links"]/@href'):
            item = LinkItem()
            link_extension = sel.extract()
            item['link'] = self.domain + link_extension
            if item['link']:
                yield scrapy.Request(item['link'], callback=self.parse_school_listing)

    # crawl each school listing
    def parse_school_listing(self, response):
        # <div class="website_text"><a>
        for sel in response.xpath('//div[@class="website_text"]/a/@href'):
            item = LinkItem()
            item['link'] = sel.extract()
            yield item
