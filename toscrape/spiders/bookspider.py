# import scrapy


# class BookspiderSpider(scrapy.Spider):
#     name = "bookspider"
#     allowed_domains = ["quotes.toscrape.com"]
#     start_urls = ["https://quotes.toscrape.com/"]

#     def parse(self, response):
#         # total = response.xpath('//div[@class="col-md-8"]/text()')

#         quote = response.xpath('//span[@class="text"]/text()').getall()
#         author = response.xpath('//small[@class="author"]/text()').getall()

#         for i in range(len(quote)):
#             yield quote[i]

#         # pass


import scrapy

class QuotesSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        
        for quote in quotes:
            text = quote.xpath('span[@class="text"]/text()').get()
            author = quote.xpath('span/small[@class="author"]/text()').get()
            tags = quote.xpath('div[@class="tags"]/a[@class="tag"]/text()').getall()
            
            yield {
                'quote': text,
                'author': author,
                'tags': tags
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
