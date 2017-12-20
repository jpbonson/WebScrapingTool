import scrapy


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

        for item in zip(titles, authors, dates, links):
            scraped_info = {
                'title': item[0],
                'author': item[1],
                'publish_date': item[2],
                'link': item[3]
            }

            yield scraped_info
