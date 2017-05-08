# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#O parenteses indica herança
class Atracao(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cidade = scrapy.Field()
    endereco = scrapy.Field()
    dia = scrapy.Field()
    hora = scrapy.Field()
    artista = scrapy.Field()
    
    #pass
