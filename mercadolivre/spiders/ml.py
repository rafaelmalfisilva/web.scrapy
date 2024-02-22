import scrapy


class MlSpider(scrapy.Spider):
    name = "ml"
    start_urls = ["https://lista.mercadolivre.com.br/auto-pecas-molina"]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="ui-search-layout__item shops__layout-item ui-search-layout__stack"]'):
            # name = i.xpath('.//h2[@class="ui-search-item__title"]/text()').get()
            linkProduct = i.xpath('.//a/@href').get()
            yield scrapy.Request(url=linkProduct, callback=self.getInfos)

    def getInfos(self, response):
        name = response.xpath('//h1[@class="ui-pdp-title"]/text()').get()
        desc = response.xpath('//div[@class="ui-pdp-description"]').getall()
        yield{
            "name": name,
            "desc": desc
        }