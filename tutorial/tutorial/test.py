# coding=utf-8
import json


file = 'items.json'
fp = open(file, 'r')
for l in fp:
    dict1 = json.loads(l)
    print dict1
fp.close()

print '哈喽'