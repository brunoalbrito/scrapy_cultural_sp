from scrapy.contrib.spiders import CrawlSpider

class ViradaCulturalSpider(CrawlSpider):
    #Nome no spider
    name = "virada_cultural"
    
    #urls onde ele vai buscar conteudos
    start_urls = ["http://www.viradaculturalpaulista.sp.gov.br/virada-cultural-paulista/"]
    
    #def parse(self, response):