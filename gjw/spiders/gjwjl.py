# -*- coding: utf-8 -*-
import scrapy
from ..items import GjwItem

class GjwjlSpider(scrapy.Spider):
    name = 'gjwjl'

    # allowed_domains = ['gjwjl.com']
    # start_urls = ['http://gjwjl.com/']
    def start_requests(self):
        url = 'http://sh.ganji.com/qiuzhi/'
        yield scrapy.Request(url=url)
    def parse(self, response):
        res=response.xpath("//div[@class='f-all-news']//i/a/@href").extract()
        for i in list(reversed(res)):
                    for j in range(100):
                        url = 'http://nj.ganji.com' + i + 'o' + str(j) + '/'
                        print(url)
                        yield scrapy.Request(url=url,callback=self.parse1)



    def parse1(self, response):
        item=GjwItem()
        for i in range(32):
            try:
                item['name'] = response.xpath('//div[@class="person fl"]/text()').extract()[i]

            except:
                item['name'] = ''

                return
            try:
                item['age'] = response.xpath('//div[@class="person fl"]/em/text()').extract()[i][2:-1]
            except:
                item['age'] = ''
            try:
                item['stu'] = response.xpath('//div[@class="basic-info"]/span[4]/text()').extract()[i]
            except:
                item['stu'] = ''
            try:
                item['work'] = response.xpath('//div[@class="basic-info"]/span[5]/text()').extract()[i]
            except:
                item['work'] = ''
            try:
                item['sex'] = response.xpath('//div[@class="person fl"]/em/text()').extract()[i][1:2]
            except:
                item['sex'] = ''
            try:
                item['address'] = response.xpath('//div[@class="s-butt s-bb1"]/ul/li[2]/text()').extract()[i]
            except:
                item['address'] = ''
            try:
                item['salary'] = response.xpath('//div[@class="s-butt s-bb1"]/ul/li[3]/text()').extract()[i]
            except:
                item['salary'] = ''
            try:
                item['towork'] = response.xpath('//div[@class="basic-info"]/span[5]/text()').extract()[i]
            except:
                item['towork'] = ''
            yield item