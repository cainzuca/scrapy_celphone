import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celular-recondicionado#D[A:celular%20recondicionado]"]

    def parse(self, response):

        bloco = response.css('div.ui-search-result__wrapper')
        
        for bloco in bloco:

            yield {
                'titulo' : bloco.css('h2.ui-search-item__title::text').get()
            }               
