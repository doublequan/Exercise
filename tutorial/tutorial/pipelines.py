# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json


class TestPipeline(object):

    def process_item(self, item, spider):

        line = json.dumps(dict(item), ensure_ascii = False) + "\n"
        #line = str(item['author']) + "\n"
        #line = json.dumps(dict(item), ensure_ascii = False, encoding='utf-8')
        #print line

        with open('items.json', 'a') as f:
            f.write(line)
        f.close()



        return item
