# -*- coding: utf-8 -*-

# Define here the models for your spider
#
#
#


import scrapy
import json

from scrapy import log
from tutorial.items import TestItem


class testSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["www.1point3acres.com"]
    start_urls = [
        "http://www.1point3acres.com/bbs/forum-82-1.html"
    ]

    def parse(self, response):

        log.msg('******Parsing Index******')

        table = response.xpath('//table[@summary = \'forum_82\']')
        tbodyList = table.xpath('//tbody')

        for i in xrange(2, len(tbodyList.extract()) + 1):
            tbody = table.xpath('tbody[' + str(i) + ']')

            author_path = tbody.xpath('tr/td[2]/cite/a/text()').extract()
            author = author_path[0].encode('utf-8') if len(author_path) != 0 else ''
            #time = tbody.xpath('tr/td[2]/em/span/text()').extract()[0].encode('utf-8')
            #status = tbody.xpath('tr/th/@class').extract()[0].encode('utf-8')
            a = tbody.xpath('tr/th/a[@class = \'s xst\']')
            a_href = a.xpath('@href').extract()[0].encode('utf-8')
            a_title = a.xpath('text()').extract()[0].encode('utf-8')

            #item = TestItem()
            #item['title'] = a_title
            #item['link'] = a_href
            #item['time'] = time
            #item['author'] = author
            #item['status'] = status
            #item['desc'] = ''
            #yield item

            yield scrapy.Request(a_href, callback=self.parseResult)


        #print (table.xpath('//tbody/@id').extract())

    '''
        JSONfile = open('items.jl', 'wb')

        line = json.dumps(tbodyList) + "\n"
        JSONfile.write(line)
    '''

    '''
        #filename = response.url.split("/")[-2]
        with open('test.txt', 'wb') as f:
            f.write(a_href + a_title)
        f.close()
    '''


    def parseResult(self, response):

        log.msg('******Parsing Result Reporting Pages******')

        postlist = response.xpath('//div[@id = \'postlist\']')
        title = postlist.xpath('//span[@id = \'thread_subject\']/text()').extract()[0].encode('utf-8')
        link = postlist.xpath('table[1]/tr/td[@class = \'plc ptm pbn vwthd\']/span[@class = \'xg1\']/a/@href').extract()[0].encode('utf-8')

        firstFloor = postlist.xpath('div[1]/table/tr/td[@class = \'plc\']')
        time = firstFloor.xpath('//div[@class = \'authi\']/em/span/@title').extract()[0].encode('utf-8')
        author = firstFloor.xpath('//div[@class = \'authi\']/a[1]/text()').extract()[0].encode('utf-8')
        author_link = firstFloor.xpath('//div[@class = \'authi\']/a[1]/@href').extract()[0].encode('utf-8')

        item = TestItem()
        #item['title'] = title
        #item['type'] = "结果汇报"
        #item['link'] = link
        #item['time'] = time
        item['author'] = author
        item['author_link'] = author_link
        yield item


#print "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/".split("/")[-2]