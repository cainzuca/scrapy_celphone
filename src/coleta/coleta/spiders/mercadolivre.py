import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celular-recondicionado#D[A:celular%20recondicionado]"]
    page_count = 1
    max_pages = 10

    def parse(self, response):

        bloco = response.css('div.ui-search-result__wrapper')
        
        for bloco in bloco:

            yield {
                'title' : bloco.css('h2.ui-search-item__title::text').get(),
                'price': bloco.css('span.andes-money-amount__fraction::text').get()
            } 


        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)  
