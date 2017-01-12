# -*- coding: utf-8 -*-
import scrapy


class EpisodesSpider(scrapy.Spider):
    name = "episodes"
    allowed_domains = [
            'itunes.apple.com/br/podcast/castalio-podcast/id446259197'
            ]
    start_urls = [
            'http://itunes.apple.com/br/podcast/castalio-podcast/id446259197/'
                ]

    def parse(self, response):
        '''O método parse concatena a variável episodes com a variável date,
        gerando assim um dicionário, onde as chaves são os nomes dos episódios
        e os valores a data no qual o mesmo foi lançado.'''

        episodes = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div/table/tbody/tr/td[2]/'
            'span/span[2]/text()').extract()

        date = response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/div/table/tbody/tr/'
            'td[4]/span/span/text()')

        castalio = {}
        for index, episode in enumerate(episodes):
            castalio[episode] = date[index].extract()
        return castalio
