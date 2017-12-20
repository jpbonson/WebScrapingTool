import scrapy
from scrapy.utils.markup import remove_tags


class TechcrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    allowed_domains = ['techcrunch.com/feed/']
    start_urls = ['http://techcrunch.com/feed/']
    custom_settings = {
        'FEED_URI': 'tmp/techcrunch.json'
    }

    def parse(self, response):
        response.selector.remove_namespaces()  # Remove XML namespaces

        titles = response.xpath('//item/title/text()').extract()
        authors = response.xpath('//item/creator/text()').extract()
        dates = response.xpath('//item/pubDate/text()').extract()
        links = response.xpath('//item/link/text()').extract()
        description = response.xpath('//item/description/text()').extract()
        categories = response.xpath('//item/category/text()').extract()

        for item in zip(titles, authors, dates, links, description, categories):
            scraped_info = {
                'title': item[0],
                'author': item[1],
                'publish_date': item[2],
                'link': item[3],
                'description': remove_tags(item[4]).replace(u'&nbsp;', u''),
                'categories': [item[5]]  # TODO: fix this, should store all categories
            }

            yield scraped_info
